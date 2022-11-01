from django.contrib import admin
from .models import Listing
from .models import ListingImage

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass

@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    pass
