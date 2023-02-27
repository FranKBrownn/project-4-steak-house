from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        Booking.objects.create(
            fname=fname,
            lname=lname,
            email=email,
            phone=phone,
            date=date,
            time=time,
        )
        return redirect('Thank_You')
    template = loader.get_template('booking.html')
    # return HttpResponse(template.render())
    return render(request, 'booking.html')


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
