FROM python:3.6

RUN pip install flask

COPY app/ /app/

WORKDIR /app

ENV READONLY 1

CMD python /app/app.py
