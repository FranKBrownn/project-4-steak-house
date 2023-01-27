from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Plublished"))


class Post(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    number = models.IntegerField()
    date = models.DateTimeField()
    notes = models.CharField(max_length=50)



