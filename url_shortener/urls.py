from django.urls import path, include
from url_shortener import views

urlpatterns = [
    path('/', views.hello_view, name='hello'),
]
