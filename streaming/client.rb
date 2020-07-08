this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'streampb')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'stream_services_pb'
require "zlib"

def  main
    hostname = 'localhost:8000'
    stub = Stream::StreamingService::Stub.new(hostname, :this_channel_is_insecure)
    begin
        track_sample = stub.get_track_audio(Stream::TrackRequest.new(idTrack: '12345', quality: nil))
    rescue GRPC::BadStatus => e
        abort "Error: #{e.message}"
    end
    File.open('./media/track2.mp3', 'w') do |destin_file|
        destin_file.write track_sample.audio  
    end


end
    
main