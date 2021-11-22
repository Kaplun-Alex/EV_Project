from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

'''
def ev_news_main(request):
    return HttpResponse('<h1>EV News page</h1>')
'''
buttons = {'About': 'About', 'Education': 'Education', 'Experience': 'Experience', 'Skills': 'Skills',
           'Courses': 'Courses', 'Background': 'Background', 'Lang': 'Lang', 'Contact': 'Contact'}


def ev_news_main(request):
    return render(request, 'ev_news/news_index.html', buttons)

