from django.urls import path
from .views import ev_news_main

urlpatterns = [
    path('', ev_news_main, name='ev_news_main'),
    ]
