# Interactive Helper

Interactive Helper - це Django веб-додаток, що дозволяє керувати контактами, новинами та відображати майбутні дні народження контактів.

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
   CLIENT_ID=ваш_client_id
   CLIENT_SECRET=ваш_client_secret
   TOKEN_URI=https://oauth2.googleapis.com/token
