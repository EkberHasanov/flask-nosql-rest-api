FROM python:3.11.1-alpine3.17

RUN apk update && apk add --no-cache && pip install --no-cache --upgrade pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

