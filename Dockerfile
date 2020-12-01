FROM alpine:3.12.0

RUN apk --update-cache \
    add musl \
    linux-headers \
    gcc \
    g++ \
    make \
    gfortran \
    openblas-dev \
    python3 \
    python3-dev \
    py3-pip

RUN pip3 install flask