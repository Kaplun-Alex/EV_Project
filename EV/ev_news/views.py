import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from ev_news.models import Headline
from requests.packages import urllib3

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

        if len(all_title) != 0:
            try:
                res = all_title.index(title)
                continue
            except ValueError:
                new_headline.save()
                print("Saved")
        else:
            new_headline.save()
            print("Saved")
    print('scrape DONE')
    return redirect("../")


def news_list(request):
    scrape(request)
    headlines = Headline.objects.all()[::-1]
    context = {'object_list': headlines, 'About': 'About', 'Education': 'Education', 'Experience': 'Experience', 'Skills': 'Skills',
           'Courses': 'Courses', 'Background': 'Background', 'Lang': 'Lang', 'Contact': 'Contact'
    }
    return render(request, "ev_news/news_index.html", context)
