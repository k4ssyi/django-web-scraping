#!/bin/bash

source .venv/bin/activate
poetry install

# cronを動かす
crontab -uroot /app/crontab
service cron restart

# 開発環境 django runserverを起動
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
