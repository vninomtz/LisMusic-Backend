this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'streampb')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'stream_services_pb'

def  main
    hostname = 'localhost:7000'
    stub = Stream::StreamingService::Stub.new(hostname, :this_channel_is_insecure)
    begin
        message = stub.get_track_audio(Stream::TrackRequest.new(idTrack: '12334', quality: nil))
        print "Enviando: #{message.audio}"
       

    rescue GRPC::BadStatus => e
        abort "Error: #{e.message}"
    end
    
end

main