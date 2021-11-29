from django.urls import path
from .views import scrape, news_list

urlpatterns = [
  path('ev_news/', scrape, name="ev_news"),
  path('', news_list, name="ev_news_home"),
]
