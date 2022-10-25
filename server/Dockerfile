FROM python:3.7-slim-stretch

WORKDIR /backend

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

RUN python3 -m pip install -r requirements.txt


EXPOSE 5000