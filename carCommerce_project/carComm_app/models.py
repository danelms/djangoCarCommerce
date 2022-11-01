import datetime
import string
import time
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

currentDate = datetime.date.today()
currentYear = currentDate.year

class Listing(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    registration = models.CharField(max_length=10)
    colour = models.CharField(max_length=50)
    year = models.IntegerField(validators=[MaxValueValidator(currentYear), MinValueValidator(1769)])
    thumbnail = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=2500)
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    
    def __str__(self) -> str:
        return self.make + " " + self.model + ", " + self.registration

class ListingImage(models.Model):
    image = models.ImageField(upload_to='images/')
    Listing = models.ForeignKey(Listing, on_delete=models.CASCADE)