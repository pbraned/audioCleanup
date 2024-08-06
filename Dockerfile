# syntax=docker/dockerfile:1

FROM python:3.11-slim
#COPY ./requirements.txt ./
RUN python3.11 -m pip install resemble-enhance --upgrade --pre
#-r requirements.txt


RUN apt update && apt-get install libgomp1 libsndfile1 -y
#WORKDIR /data

RUN python3.11 -m pip install flask
COPY ./app /app
WORKDIR /app
RUN mkdir -p /app/uploads /app/output

CMD flask run --host=0.0.0.0 --port=5000
EXPOSE 5000
