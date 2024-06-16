FROM python:3.9

RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /app

COPY . ./

ENTRYPOINT [ "python3", "-u", "mtu_finder.py"]