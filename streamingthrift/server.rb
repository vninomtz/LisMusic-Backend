$:.push('gen-rb')
require 'thrift'
require 'streaming_service'
require 'securerandom'
require 'rest-client'
require 'json'
require "mp3info"

AUTH_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiNjhkZmIyMjAtYTRiMC00MzU3LTg5MWEtMmJlOWQ1YWYxNWNkIiwiZXhwIjpudWxsfQ.0jcKlKShoddsT1-M4h7bMkJfpQAg7RdF21D8zJq7a7I"
URL = "http://0.0.0.0:5000/track"

def get_length_track(filename)
    Mp3Info.open("../streaming/media/#{filename}.mp3") do |mp3info|
        return mp3info.length.to_i
      end
end

def save_filename_track(id_track,filename)
    begin     
        RestClient::Request.execute(
            method: :put,
            url: URL,
            payload: {"idTrack": id_track,
                    "title": nil,
                    "duration": get_length_track(filename),
                    "reproductions": nil,
                    "fileTrack": filename,
                    "available": 1,
                    "idAlbum": nil}.to_json,
            headers: {"Content-Type" => "application/json",
                    "Authorization" => AUTH_TOKEN }
           )
        return true
    rescue => exception
        print exception
        return false 
    end  
end

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
        save_filename_track(trackAudio.idTrack, fileName) 
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




