# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /code

COPY . /code

ENTRYPOINT ["python3"]
CMD ["app_malicious.py"]
