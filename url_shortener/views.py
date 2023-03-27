from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.utils import timezone
from .models import Link, Visit, VisitStatistics
from .services import get_short_url_hash, get_ip_address
from .forms import UrlForm


def short_url_view(request):
    """
    Display a form for entering url address to make short version on GET request and create new :model:`url_shortener.Link` from form data on POST request.

    **Context**
    ``form``
        A form :form:`url_shortener.UrlForm`.
    ``error_message``
        Message for validation error. 

    **Template:**

    :template:`url_shortener/url_form.html`
    """
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
    """
    Redirect user to initial url addres when user request the resource using short link (domain name + url token)
    and update the visits counter:
    - get user IP address
    - create new :model:`url_shortener.Visit`.
    - update :model:`url_shortener.VisitStatistics`.

    **Redirect:**

    :field:`url_shortener.Link.full_url`
    """
    link = Link.objects.filter(slug=token).first()
    ip_address = get_ip_address(request)
    Visit.objects.create(ip_address=ip_address, link=link)
    statistics = link.statistics
    statistics.total_visits = statistics.total_visits + 1
    statistics.save()
    return redirect(link.full_url)

def statistics_view(request):
    """
    Display statistics on visiting urls stored in daat base - list of :model:`url_shortener.VisitStatistics`.

    **Context**
    ``links``
        A list of :model:`url_shortener.Link`.

    **Template:**

    :template:`url_shortener/statistics.html`
    """
    links = Link.objects.all()
    context = { 'links': links }
    return render(request, 'statistics.html', context)