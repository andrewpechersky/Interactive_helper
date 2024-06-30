# Interactive Helper

Interactive Helper - це Django веб-додаток, що дозволяє керувати контактами, нотатками, файлами та відображати майбутні дні народження контактів.

## Встановлення

1. Клонування репозиторію:

   ```bash
   git clone https://github.com/ваш-юзернейм/interactive_helper.git
   cd interactive_helper
2. Створення та активація віртуального середовища:
    ```bash
   python -m venv env
   source env/bin/activate # для Windows: .\env\Scripts\activate
3. Встановлення необхідних пакетів:
   ```bash
   pip install -r requirements.txt
4. Налаштування змінних середовища:
Створіть файл .env в кореневій директорії проекту і додайте наступні змінні:
   ```bash
   EMAIL_HOST=smtp сервер
   EMAIL_PORT=порт серверу
   EMAIL_HOST_USER=імейл@мейл.ком
   EMAIL_HOST_PASSWORD=пароль
   SECRET_KEY=ваш_client_secret
   CLIENT_ID=ваш_client_id google
   CLIENT_SECRET=ваш_client_secret google
   TOKEN_URI=https://oauth2.googleapis.com/token
5. Створення та міграція бази даних:
   ```bash
   python manage.py makemigrations files
   python manage.py makemigrations contacts
   python manage.py makemigrations notes
   python manage.py migrate
6. Створення суперкористувача для адміністрування:
   ```bash
   python manage.py createsuperuser
7. Запуск сервера:
   ```bash
   python manage.py runserver 127.0.0.1:8000