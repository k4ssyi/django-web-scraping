FROM python:3.7
WORKDIR /app

ENV PYTHONPATH /app/
ENV LANG en_US.utf8
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

RUN apt-get -y update \
    && apt-get -y upgrade
RUN apt-get -y install vim cron

RUN pip install --upgrade pip setuptools wheel \
    && pip install poetry \
    && poetry config settings.virtualenvs.in-project true

ADD . /app
