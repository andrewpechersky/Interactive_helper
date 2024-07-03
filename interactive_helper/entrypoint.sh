#!/bin/bash

# Збірка статичних файлів
python manage.py collectstatic --noinput

# Запуск сервера
gunicorn contacts_project.wsgi:application --bind 0.0.0.0:$PORT
