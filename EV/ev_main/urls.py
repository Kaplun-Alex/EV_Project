from django.urls import path
from .views import port

urlpatterns = [
    path('', port, name='main'),
]
