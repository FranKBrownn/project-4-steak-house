from . import views
from django.urls import path


urlpattens = [
    path('booking/', views.PostBooking.as_view(), name='home')
]