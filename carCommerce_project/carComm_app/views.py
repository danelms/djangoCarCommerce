from django.shortcuts import render
from django.http import Http404
from .models import Listing, ListingImage, Queries

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

def carDetails(request, registration):
    try:
        listing = Listing.objects.get(registration=registration)
        listingImages = ListingImage.objects.filter(listing_id=listing.id)
    except Listing.DoesNotExist:
        raise Http404("Car with registration \"" + registration + "\" not found")

    return render(request, 'carDetails.html', {'listing': listing, 'listingImages': listingImages})

