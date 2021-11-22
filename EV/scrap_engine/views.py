from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from scrap_engine.models import Headline
from requests.packages import urllib3


def scrapapp_plug(request):
    return HttpResponse('<h1>SCRAP ENGINE</h1>')


def scrapapp_main(request):
    return render(request, 'scrap_engine/scrapapp.html')


requests.packages.urllib3.disable_warnings()


def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.firstpost.com/tag/electric-scooter"
    content = session.get(url, verify=False).content
    #print('CONTENT', content)
    soup = BSoup(content, "html.parser")
    print('SOUP', soup)
    news = soup.find_all('div', {"class": "big-thumb"})
    #print('NEWS', news)
    for article in news:
        print('Перебор', article)
        main = article.find_all('a')[0]
        link = main['href']
        image_src = str(main.find('img')['srcset']).split(" ")[-4]
        title = main['title']
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
    return redirect("../")


def news_list(request):
    #print("I'm work dude")
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    #print('Context', context)
    return render(request, "scrap_engine/scrapapp.html", context)
