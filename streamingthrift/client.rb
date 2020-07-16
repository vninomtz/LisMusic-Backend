$:.push('gen-rb')
require 'thrift'
require 'streaming_service'


transport = Thrift::BufferedTransport.new(Thrift::Socket.new('localhost', 8000))
protocol = Thrift::BinaryProtocol.new(transport)
client = StreamingService::Client.new(protocol)

transport.open()

track_audio = client.GetTrackAudio(TrackRequest.new(idTrack: 43, quality: nil))

File.open('../streaming/media/track3.mp3', 'w') do |destin_file|
        destin_file.write track_audio.audio
    
end

transport.close()