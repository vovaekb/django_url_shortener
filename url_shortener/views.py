from django.shortcuts import render, HttpResponse
from .models import Link, Visit
from .services import short_url


def short_url(request):
    if request.method == 'POST':
        pass
    else:
        url = request.get('url')
        url_hash = short_url()
        return HttpResponse('short url', 200)

def redirect_url(request):
    return HttpResponse('redirect url', 200)

def statistics_view(request):
    return HttpResponse('statistics', 200)