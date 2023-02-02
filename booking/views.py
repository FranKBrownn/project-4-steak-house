from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from .models import Post


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render()) 


def booking(request):
    template = loader.get_template('booking.html')
    return HttpResponse(template.render()) 


def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())         


