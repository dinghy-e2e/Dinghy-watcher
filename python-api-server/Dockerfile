# FROM alpine:3.17
# RUN apk add python3 py3-pip && pip install boto3 

FROM ubuntu:lunar
RUN apt update && apt upgrade -y && apt install -y python3 pip && pip install boto3 psutil flask requests

WORKDIR /app
COPY . .
COPY ./credentials /root/.aws/credentials
CMD [ "python3", "main.py" ]