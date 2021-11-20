from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse('<h1>EV Main page</h1>')


def port(request):
    return render(request, 'ev_main/main_index.html')
