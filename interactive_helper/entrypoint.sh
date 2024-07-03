#!/bin/bash

# Збірка статичних файлів
python manage.py collectstatic --noinput

# Запуск сервера
gunicorn interactive_helper.wsgi:application --bind 127.0.0.1:$PORT
