FROM golang:1.9
MAINTAINER Mike Heijmans <parabuzzle@gmail.com>

RUN mkdir -p /build
ENV GOPATH=/go

RUN apt-get update && apt-get install -y zip

RUN go get -u -v github.com/ChimeraCoder/gojson/gojson && \
    go get -u -v github.com/golang/protobuf/protoc-gen-go && \
    go get -u -v github.com/gogo/protobuf/protoc-gen-gofast && \
    go get -u github.com/golang/dep/cmd/dep && \
    go get -u -v golang.org/x/tools/cmd/stringer

RUN wget https://github.com/google/protobuf/releases/download/v3.1.0/protoc-3.1.0-linux-x86_64.zip && \
    unzip protoc-3.1.0-linux-x86_64.zip && \
    cp bin/protoc /usr/bin/protoc && \
    chmod 777 /usr/bin/protoc

WORKDIR /go/src/github.com/stripe/veneur

RUN wget https://github.com/stripe/veneur/archive/master.zip && \
    unzip master.zip && \
    mv veneur-master/* .

RUN rm -rf master.zip

RUN dep ensure -v
RUN gofmt -w .

RUN go test -race -v -timeout 60s ./... && \
    go build -a -v -ldflags "-X github.com/stripe/veneur.VERSION=latest" -o /build/veneur ./cmd/veneur

ADD generate_config.py /go/src/github.com/stripe/veneur/
ADD run.sh /go/src/github.com/stripe/veneur/
RUN chmod 777 /go/src/github.com/stripe/veneur/run.sh

CMD /go/src/github.com/stripe/veneur/run.sh
