FROM ubuntu:latest
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gcc make xinetd

RUN rm /etc/xinetd.d/*
COPY cfg /etc/xinetd.d/addition

COPY addition.c /
COPY Makefile /
WORKDIR /
RUN make
RUN mv addition /bin

CMD ["/usr/sbin/xinetd", "-dontfork"]
