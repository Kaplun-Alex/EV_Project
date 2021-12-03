from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ev_main.urls')),
    path('ev_main/', include('ev_main.urls')),
    path('ev_news/', include('ev_news.urls')),
    path('ev_shop/', include('ev_shop.urls')),
    path('scrapapp/', include('scrap_engine.urls')),
]
