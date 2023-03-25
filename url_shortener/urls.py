from django.urls import path, include
from url_shortener import views

urlpatterns = [
    path('short/', views.short_url, name='short_url'),
    path('redirect_url', views.redirect_url, name='redirect_url'),
    path('statistics/', views.statistics_view, name='statistics'),
]
