
FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y ruby \
    bundler \
    ri \
    ruby-dev
RUN gem install thrift
COPY ./streamingthrift ./streamingservice/streamingthrift
COPY ./streaming ./streamingservice/streaming
WORKDIR /streamingservice/streamingthrift
CMD ruby server.rb
EXPOSE 8000