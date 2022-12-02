from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, PurchaseForm
from .models import Listing, ListingImage, Queries
from .filters import ListingFilter

def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings':listings})

def listings(request):
    uniqueColours = Queries.uniqueColours()
    uniqueMakes = Queries.uniqueMakes()
    listings = Listing.objects.all()
    listingFilter = ListingFilter(request.GET, queryset=listings)
    return render(request, 'listings.html', {'listings':listings, 'uniqueColours':uniqueColours, 'uniqueMakes':uniqueMakes, 'listingFilter': listingFilter})

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
            email = form.cleaned_data['email_address']
            confirmation = "Thank you! Your email has been submitted and you should hear back from us within 2 working days."
            try:
                send_mail("Web enquiry", message, email, ['enquiries@carcommerce.uk'])
                newForm = ContactForm()
                return render(request, 'contact.html', {'contactForm': newForm, 'confirmation': confirmation})
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            confirmation = "Sorry, we were unable to submit this email. Did you complete the reCAPTCHA above?"
            return render(request, 'contact.html', {'contactForm': form, 'confirmation': confirmation})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'contactForm': form})

def purchaseForm(request, registration):
    try:
        listing = Listing.objects.get(registration=registration)
    except Listing.DoesNotExist:
        raise Http404("Car with registration \"" + registration + "\" not found")
    
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            body = {
            'car': listing.__str__(),
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email_address'],
            'phone': form.cleaned_data['phone'].__str__(),
            }
            message = "\n".join(body.values())
            email = form.cleaned_data['email_address'],
            confirmation = "Thank you! Your purchase request has been sent. We will mark the " + listing.make + " " + listing.model + " as 'sold pending payment' and call within 2 working days to arrange payment and collection."
            try:
                send_mail("Purchase enquiry", message, email, ['sales@carcommerce.uk'])
                newForm = PurchaseForm
                return render(request, 'purchaseForm.html', {'purchaseForm': newForm, 'confirmation': confirmation})
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            confirmation = "Sorry, we were unable to submit this purchase request. Did you complete the reCAPTCHA above?"
            return render(request, 'purchaseForm.html', {'purchaseForm': form, 'confirmation': confirmation})
    else:
        form = PurchaseForm()
    return render(request, 'purchaseForm.html', {'purchaseForm': form, 'listing': listing})
        

def carDetails(request, registration):
    try:
        listing = Listing.objects.get(registration=registration)
        listingImages = ListingImage.objects.filter(listing_id=listing.id)
    except Listing.DoesNotExist:
        raise Http404("Car with registration \"" + registration + "\" not found")

    return render(request, 'carDetails.html', {'listing': listing, 'listingImages': listingImages})

