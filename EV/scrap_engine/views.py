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
    url = "https://electrek.co/guides/electric-motorcycle/"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "lxml")
    news = soup.find_all('article', {"class": "post-content"})
    all_title = []
    list_of_title = Headline.objects.all()
    for i in list_of_title:
        all_title.append(i.title)
    print(all_title)
    for article in news:
        image_src = str(article.find('img')['srcset']).split(" ")[-4]
        title = article.find('a').getText()
        link = article.find('a').get("href")
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        print(type(title))

        if len(all_title) != 0:
            res = all_title.index(title)
            if res < 0:
                new_headline.save()
                print("Saved")
            else:
                print('go to hel')
        else:
            new_headline.save()
    return redirect("../")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "scrap_engine/scrapapp.html", context)
