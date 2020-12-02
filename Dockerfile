FROM alpine:3.12.0

RUN apk --update-cache \
    add musl \
    linux-headers \
    curl \
    gcc \
    g++ \
    make \
    gfortran \
    openblas-dev \
    python3 \
    py3-pip \
    mysql \
    mysql-client \
    openrc \
    build-base \
    mariadb-connector-c-dev \
    python3-dev

RUN mkdir /run/openrc \
    touch /run/openrc/softlevel
RUN /etc/init.d/mariadb setup
RUN rc-status
RUN pip3 install flask flask-cors mysqlclient

ENV FLASK_ENV development