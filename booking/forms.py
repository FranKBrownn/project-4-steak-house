from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        feilds = ['fname', 'lname', 'email', 'number', 'date', 'time', 'notes']