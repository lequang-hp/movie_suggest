FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update \
    && apt-get clean

WORKDIR /app

ENV PYTHONPATH /app

RUN pip install pipenv && pipenv --version

COPY . /app

RUN pipenv install --system --deploy

RUN chmod +x prestart.sh tests/test.sh

EXPOSE 5000