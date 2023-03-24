from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Booking(models.Model):
    Name = models.CharField(max_length=15, blank=False)
    Email = models.EmailField(unique=True, blank=False)
    Phone = models.IntegerField(blank=False)
    Date = models.DateField(blank=False)
    Time = models.TimeField(blank=False)
    Notes = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.fname



