from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Plublished"))


class Post(models.Model):
    fname = models.CharField(max_length=15, blank=False)
    lname = models.CharField(max_length=15, blank=False)
    email = models.EmailField(unique=True, blank=False)
    number = models.IntegerField(blank=False)
    date = models.DateTimeField(blank=False)
    notes = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.fname



