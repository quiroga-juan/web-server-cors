# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /malicious

COPY malicious/requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt


COPY malicious/ .

RUN cat app_malicious.py

CMD python3 app_malicious.py
