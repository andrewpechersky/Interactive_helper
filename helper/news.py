from bs4 import BeautifulSoup
import requests

def parse_news(html_content):
    try:
        # Створюємо об'єкт BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Знаходимо всі елементи з класом 'card card_media'
        news_cards = soup.find_all(class_='card card_media')

        news_list = []  # Список для зберігання інформації про новини

        # Цикл для кожного контейнера новини (10 перших новин)
        for card in news_cards[:10]:
            # Знаходимо посилання на саму новину
            news_link = card.find(class_='card__link')['href']

            # Знаходимо заголовок новини
            title = card.find(class_='card__title').text.strip()

            # Знаходимо посилання на фото
            img_url = card.find('img')['src']


            # Додаємо інформацію про новину до списку
            news_list.append({
                'title': title,
                'img_url': "http://dev.ua" + img_url,
                'news_link': news_link,

            })

        return news_list
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    url = 'https://dev.ua/news'

    # Отримуємо HTML вміст сторінки
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
        return

    html_content = response.text

    # Викликаємо функцію parse_news з вхідним HTML-контентом і отримуємо результат
    parsed_news = parse_news(html_content)

    if parsed_news:
        # Виводимо результати
        for idx, news in enumerate(parsed_news, start=1):
            print(f"Новина #{idx}:")
            print(f"Назва: {news['title']}")
            print(f"Посилання на фото: {news['img_url']}")
            print(f"Посилання на новину: {news['news_link']}")
            print()
    else:
        print("Failed to parse news.")

if __name__ == "__main__":
    main()
