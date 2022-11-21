from django.shortcuts import render, redirect
from django.http import Http404
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email_address'],
            'subject': form.cleaned_data['subject'],
            'message':form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(message, 'danelms@live.co.uk', ['danelms@live.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return redirect (request, "home.html")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'contactForm': form})

def carDetails(request, registration):
    try:
        listing = Listing.objects.get(registration=registration)
        listingImages = ListingImage.objects.filter(listing_id=listing.id)
    except Listing.DoesNotExist:
        raise Http404("Car with registration \"" + registration + "\" not found")

    return render(request, 'carDetails.html', {'listing': listing, 'listingImages': listingImages})

