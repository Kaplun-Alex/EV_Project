import requests
from bs4 import BeautifulSoup as BSoup

def scrape():
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.unian.ua/detail/main_news"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    print(soup)


scrape()
