from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from .models import Booking
from .forms import BookingForm


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
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Thank_You')
    form = BookingForm() 

    context = {
        'form': form
    }  
    template = loader.get_template('booking.html')
    # return HttpResponse(template.render())
    return render(request, 'booking.html', context)


def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())  


def Thank_You(request):
    template = loader.get_template('thank_you.html')
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
