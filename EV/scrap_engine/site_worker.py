import requests
from bs4 import BeautifulSoup as BSoup


url = "https://www.greencarreports.com/news/electric-cars"


def get_data(url): # get request
    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    req = requests.get(url, headers)
    print(req.text)
    with open("ev_cars.html", "w") as file:
        file.write(req.text)




def trash():
    with open("ev_cars.html", "r") as file:
        src = file.read()
    soup = BSoup(src, "lxml")
    dec = (['desktop-newsletter', 'large', "nativo-slot"])

    for i in soup.find_all("li", {'class': 'desktop-newsletter'}):
        i.decompose()
    stt = soup.find_all('li')
    for i in stt:
        print(i)
        print("********************************************************************")

trash()
