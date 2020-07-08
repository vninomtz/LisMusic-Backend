#!/usr/bin/env ruby

this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'streampb')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'stream_services_pb'
require 'rest-client'
require 'json'

class TrackSampleEnum
    def initialize(listSamples)
        @samples = listSamples
    end

    def each
        return enum_for(:each) unless block_given?
        begin
            @samples.each do |sample|
                yield Stream::TrackSample.new(audio: sample)
            end
            
        rescue StandarError => e
            fail e
        end
    end
end

def get_track(idTrack)
    puts "Me llegó el track #{idTrack}"
    response = RestClient.get("http://0.0.0.0:6000/track/#{idTrack}")
    results = JSON.parse(response.to_str)
    file = results['fileTrack']
    return file
end


class StreamingServer < Stream::StreamingService::Service    
    def get_track_audio(track_request, _unused_call)
        idTrack = track_request.idTrack
        name = get_track(idTrack)
        listSamples = []
        File.open "./media/#{name}", "r" do |source_file|
            until source_file.eof?
                chunk = source_file.read 100000 
                listSamples.push(chunk) 
            end
        end
        TrackSampleEnum.new(listSamples).each
    end
end


def main
    server = GRPC::RpcServer.new
    server.add_http2_port('0.0.0.0:8000', :this_port_is_insecure)
    server.handle(StreamingServer)
    puts "Server running in 0.0.0.0:8000"
    server.run_till_terminated_or_interrupted([1, 'int', 'SIGQUIT'])
end

main