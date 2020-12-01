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
    py3-pip

RUN pip3 install flask flask-cors

ENV FLASK_ENV development