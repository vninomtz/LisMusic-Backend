this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'streampb')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'stream_services_pb'
require "zlib"

def  main
    hostname = 'localhost:8000'
    audio = []
    stub = Stream::StreamingService::Stub.new(hostname, :this_channel_is_insecure)
    begin
        track_sample = stub.get_track_audio(Stream::TrackRequest.new(idTrack: '004a2196-c2ae-44e0-9e03-ff36d2b7164b', quality: nil))
        track_sample.each do |chunk|
            audio << chunk.audio
        end
    rescue GRPC::BadStatus => e
        abort "Error: #{e.message}"
    end
   
    File.open('./media/track2.mp3', 'w') do |destin_file|
        audio.each do |chunk|
            destin_file.write chunk
        end
    end


end
    
main