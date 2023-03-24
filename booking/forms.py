from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['Name', 'Email', 'Phone', 'Date', 'Time', 'Notes']