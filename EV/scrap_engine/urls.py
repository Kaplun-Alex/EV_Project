from django.urls import path
from .views import scrapapp_main, scrapapp_plug
'''
urlpatterns = [
    path('', scrapapp_plug, name='scrapapp'),
]
'''
from django.urls import path
from scrap_engine.views import scrape, news_list

urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', news_list, name="home"),
]