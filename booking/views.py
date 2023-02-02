from django.shortcuts import render
from django.views import generic
from .models import Post


class PostBooking(generic.ListView):
    template_name = 'booking.html.'

