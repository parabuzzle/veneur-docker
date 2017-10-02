FROM golang:1.9
MAINTAINER Mike Heijmans <parabuzzle@gmail.com>

RUN mkdir -p /application
ENV GOPATH=/go

WORKDIR /application

ADD ./generate_config.py ./generate_config.py
ADD ./run.sh ./run.sh
ADD ./veneur ./veneur
RUN chmod 777 ./run.sh

CMD ./run.sh
