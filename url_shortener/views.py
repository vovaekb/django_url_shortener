from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.utils import timezone
from .models import Link, Visit, VisitStatistics
from .services import get_short_url_hash, get_ip_address
from .forms import UrlForm


def short_url_view(request):
    form = UrlForm
    if request.method == 'POST':
        if form.is_valid():
            url = request.POST['url']
            url_token = get_short_url_hash()
            print('url: ', url, ', url_hash:', url_token)
            server_uri = request.build_absolute_uri('/')
            short_url = f'{server_uri}{url_token}'
            context = {
                'short_url': short_url
            }
            statistics = VisitStatistics.objects.create()
            link_object = Link.objects.create(full_url=url, slug=url_token, statistics=statistics)
        else:
            error_message = 'Невалидный ввод URL адреса'
    else:
        error_message = ''
        server_uri = request.build_absolute_uri('/')
        print('server_uri: ', server_uri)
        context = {
            'form': form,
            'error_message': error_message
        }
    return render(request, 'url_form.html', context)

def redirect_url(request, token):
    link = Link.objects.filter(slug=token).first()
    print('link: ', link.full_url)
    ip_address = get_ip_address(request)
    Visit.objects.create(ip_address=ip_address, link=link)
    statistics = link.statistics
    statistics.total_visits = statistics.total_visits + 1
    statistics.save()
    print('total_visits: ', statistics.total_visits)
    return HttpResponse('redirect_url', 200)
    # return redirect(link.full_url)

def statistics_view(request):
    links = Link.objects.all()
    context = { 'links': links }
    return render(request, 'statistics.html', context)