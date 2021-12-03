from django.urls import path
from .views import scrape, news_list
from .api import HeadlineViewSet
from rest_framework import routers

urlpatterns = [
  path('ev_news/', scrape, name="ev_news"),
  path('', news_list, name="ev_news_home"),
]

router = routers.DefaultRouter()
router.register('api/news', HeadlineViewSet, 'news')
urlpatterns += router.urls
