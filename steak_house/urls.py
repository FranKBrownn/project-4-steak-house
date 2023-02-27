"""steak_house URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking.views import index, home, menu, gallery, booking, MenuFoodWine , Thank_You

urlpatterns = [
    path('', index, name='home'),
    path('templates/index.html/', home, name='home'),
    path('templates/menu.html/', menu, name='home'),
    path('templates/gallery.html', gallery, name='gallery'),
    path('templates/booking.html/', booking, name='home'),
    path('static/menus/arch_steak_house_food.pdf', MenuFoodWine, name='foodmenu'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('templates/booking.html/add', Thank_You, name='thank_you' )
    
]
