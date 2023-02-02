from . import views
from django.urls import path


urlpattens = [
    path('', views.index, name='home'),
]