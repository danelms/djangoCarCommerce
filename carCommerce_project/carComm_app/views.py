from django.shortcuts import render
from .models import Listing

def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings':listings})

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings':listings})

