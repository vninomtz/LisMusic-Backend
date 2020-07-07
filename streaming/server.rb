#!/usr/bin/env ruby

this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'streampb')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'stream_services_pb'

class StreamingServer < Stream::StreamingService::Service
    def get_track_audio(track_request,_unused_call)
        idTrack = track_request.idTrack
        print 'El track es: ',idTrack
        
        track_sample = Stream::TrackSample.new(audio: "1010101")
        puts track_sample.audio
        return track_sample
        
    end
    
end


def main
    server = GRPC::RpcServer.new
    server.add_http2_port('0.0.0.0:7000', :this_port_is_insecure)
    server.handle(StreamingServer)
    print 'Grpc streaming server is running'
    server.run_till_terminated_or_interrupted([1, 'int', 'SIGQUIT'])
end

main