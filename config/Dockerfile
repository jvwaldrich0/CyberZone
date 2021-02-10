FROM python:3.9.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

