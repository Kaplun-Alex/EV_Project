from django.urls import path
from .views import ev_shop_main

urlpatterns = [
    path('', ev_shop_main, name='ev_shop_main'),
    ]