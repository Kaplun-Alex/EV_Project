from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

'''
def ev_shop_main(request):
    return HttpResponse('<h1>EV Shop page</h1>')
'''


def ev_shop_main(request):
    return render(request, 'ev_shop/shop_index.html')
