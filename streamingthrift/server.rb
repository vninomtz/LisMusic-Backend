$:.push('gen-rb')
require 'thrift'
require 'streaming_service'
require 'rest-client'
require 'json'

def get_track(idTrack)
    puts "Me llegó el track #{idTrack}"
    response = RestClient.get("http://0.0.0.0:6000/track/#{idTrack}")
    results = JSON.parse(response.to_str)
    file = results['fileTrack']
    return file
end

class StreamingServiceHander
    def GetTrackAudio(trackRequest)
        puts("andamos on")
        puts(trackRequest.idTrack)
        audio = ''
        File.open "../streaming/media/track1.mp3", "r" do |source_file|
            until source_file.eof?
                chunk = source_file.read 100000 
                audio = audio + chunk
            end
        end
        track_audio = TrackAudio.new(audio: audio)
        puts 'morirá aquí'
        print track_audio.audio
        
        File.open('../streaming/media/track2.mp3', 'wb') do |destin_file|
            destin_file.write audio
        end

        
        
        return track_audio
    end
end
    
 

handler = StreamingServiceHander.new()
processor = StreamingService::Processor.new(handler)
transport = Thrift::ServerSocket.new(8000)
transportFactory = Thrift::BufferedTransportFactory.new()
server = Thrift::SimpleServer.new(processor, transport, transportFactory)
puts "Server is running in 8000"
server.serve()
puts "done."