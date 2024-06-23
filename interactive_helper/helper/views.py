# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .news import parse_news  # імпортуємо функцію parse_news з news.py
import requests

def main(request):
    url = 'https://dev.ua/news'

    # Отримуємо HTML вміст сторінки
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponse(f'Failed to retrieve the webpage. Status code: {response.status_code}')

    html_content = response.text

    # Викликаємо функцію parse_news з вхідним HTML-контентом і отримуємо результат
    parsed_news = parse_news(html_content)

    if parsed_news:
        context = {
            'news_list': parsed_news
        }
        return render(request, 'helper/index.html', context)
    else:
        return HttpResponse('Failed to parse news.')





    #return render(request, "helper/index.html")
