FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /mail

COPY Pipfile Pipfile.lock /mail/

RUN pip install pipenv && pipenv install --system

COPY . /mail/