import datetime
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
    mileage = models.IntegerField(validators=[MinValueValidator(1)])
    thumbnail = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=2500)
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    pending_sale = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.make + " " + self.model + ", " + self.registration

    def getColour(self) -> str:
        return self.colour

class ListingImage(models.Model):
    image = models.ImageField(upload_to='images/')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.listing.make + " " + self.listing.model + ", " + self.listing.registration

class Queries(models.Model):
    def uniqueColours() -> list:
        uniqueColours = Listing.objects.all().order_by('colour').values_list('colour', flat=True).distinct()

        return uniqueColours

    def uniqueMakes() -> list:
        uniqueMakes = Listing.objects.all().order_by('make').values_list('make', flat=True).distinct()
        
        return uniqueMakes

