FROM python:3.9

WORKDIR /src
RUN apt-get update && pip install --upgrade pip

RUN pip install celery redis

COPY . /src
