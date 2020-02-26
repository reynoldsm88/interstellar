FROM docker.causeex.com/dart/image-playground:latest
LABEL maintainer="michael.reynolds@twosixlabs.com"

RUN mkdir -p /opt/app/interstellar/interstellar

COPY *.py /opt/app/interstellar/
COPY interstellar/* /opt/app/interstellar/interstellar/
COPY Makefile /opt/app/interstellar
COPY requirements.txt /opt/app/interstellar
COPY README.md /opt/app/interstellar
COPY LICENSE /opt/app/interstellar

RUN cd /opt/app/interstellar && \
    make python-build

ENTRYPOINT /bin/bash