from django.urls import path
from .views import index, port

urlpatterns = [
    path('', index, name='main'),
    path('port/', port, name='port'),
]