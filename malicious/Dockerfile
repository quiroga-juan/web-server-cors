# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /code

COPY . /code
RUN mkdir hola
RUN file="$(ls)" && echo $file
