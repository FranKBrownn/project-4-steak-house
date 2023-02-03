from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from .models import Booking


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())


# def MakeBooking(request):
#     if request.method == 'POST':


def booking(request):
    template = loader.get_template('booking.html')
    return HttpResponse(template.render()) 


def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())         


def MenuFoodWine(request):
    template = loader.get_template('/static/menus/arch_steak_house_food.pdf')
    return HttpResponse(template.render())


def MenuPudding(request):
    template = loader.get_template('')
    return HttpResponse(template.render())  


def MenuDrinks(request):
    template = loader.get_template('')
    return HttpResponse(template.render())  
