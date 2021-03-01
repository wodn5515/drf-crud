FROM python:3.8.5-buster
ENV PYTHONUBBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
