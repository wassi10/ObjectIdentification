from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='homepage'),
    path('result-page', views.Result, name='result-page'),
]