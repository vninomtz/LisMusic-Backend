#!/usr/bin/env ruby

this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'streampb')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'stream_services_pb'

class TrackSampleEnum
    def initialize(listSamples)
        @samples = listSamples
    end

    def each
        return enum_for(:each) unless block_given?
        begin
            @samples.each do |sample|
                print "Enumerable"
                yield Stream::TrackSample.new(audio: sample)
            end
            
        rescue StandarError => e
            fail e
        end
    end
end


class StreamingServer < Stream::StreamingService::Service    
    def get_track_audio(track_request,_unused_call)
        idTrack = track_request.idTrack
        puts 'El track es: ',idTrack
        #track_sample = Stream::TrackSample.new(audio: nil)
        
        listSamples = []
        File.open "./media/track1.mp3", "r" do |source_file|
            until source_file.eof?
                chunk = source_file.read 100000 
                #track_sample.audio = track_sample.audio + chunk 
                
                listSamples.push(chunk) 
            end
        end
        puts "#{
            listSamples.length}"
        #return track_sample
        TrackSampleEnum.new(listSamples).each
    end
end


def main
    server = GRPC::RpcServer.new
    server.add_http2_port('0.0.0.0:8000', :this_port_is_insecure)
    server.handle(StreamingServer)
    print 'Grpc streaming server is running'
    server.run_till_terminated_or_interrupted([1, 'int', 'SIGQUIT'])
end

main