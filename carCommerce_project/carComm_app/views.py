from django.shortcuts import render
from .models import Listing, Queries

def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings':listings})

def listings(request):
    uniqueColours = Queries.uniqueColours()
    uniqueMakes = Queries.uniqueMakes()
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings':listings, 'uniqueColours':uniqueColours, 'uniqueMakes':uniqueMakes})

def contact(request):
    return render(request, 'contact.html')

def carDetails(request):
    return render(request, 'carDetails.html')

