from django.urls import path, include
from url_shortener import views

urlpatterns = [
    path('short/', views.short_url_view, name='short_url'),
    path('<str:token>', views.redirect_url, name='redirect_url'),
    path('statistics/', views.statistics, name='statistics'),
    path('excel_export/', views.excel_export, name='excel_export'),
]
