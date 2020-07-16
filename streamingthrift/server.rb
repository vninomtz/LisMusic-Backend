$:.push('gen-rb')
require 'thrift'
require 'streaming_service'
require 'securerandom'

class StreamingServiceHander
    def GetTrackAudio(trackRequest)
        audio = ''
        File.open "../streaming/media/#{trackRequest.fileName}.mp3", "r" do |source_file|
            until source_file.eof?
                chunk = source_file.read 100000 
                audio = audio + chunk
            end
        end
        track_audio = TrackAudio.new(audio: audio)
        return track_audio
    end

    def UploadTrack(trackAudio)         
        fileName = trackAudio.trackName + SecureRandom.hex(5)
        File.open("../streaming/media/#{fileName}.mp3", 'wb') do |destin_file|
            destin_file.write trackAudio.audio
        end
        track_uploaded = TrackUploaded.new(fileName: fileName)
        return track_uploaded
    end
end

handler = StreamingServiceHander.new()
processor = StreamingService::Processor.new(handler)
transport = Thrift::ServerSocket.new(8000)
transportFactory = Thrift::BufferedTransportFactory.new()
server = Thrift::SimpleServer.new(processor, transport, transportFactory)
puts "Rpc Streaming server is running in 8000"
server.serve()