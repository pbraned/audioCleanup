FROM python:3.11-slim
RUN python3.11 -m pip install resemble-enhance --upgrade
WORKDIR /data

#RUN python3.11 -m pip install flask
#COPY ./app /app
#WORKDIR /app
#CMD flask run --host=0.0.0.0 --port=5000
#EXPOSE 5000
