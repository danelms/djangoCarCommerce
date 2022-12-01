import django_filters
from .models import Listing, Queries

class ListingFilter(django_filters.FilterSet):

    make = django_filters.ChoiceFilter(lookup_expr='iexact',empty_label="All makes")
    colour = django_filters.ChoiceFilter(lookup_expr='iexact',empty_label="All colours")
    mileage__lt = django_filters.NumberFilter(field_name='mileage', lookup_expr='lte',label="Maximum mileage") 
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte',label="Maximum price") 

    class Meta:
        model = Listing
        fields = ['make', 'colour']

    def __init__(self, *args, **kwargs):
        super(ListingFilter, self).__init__(*args, **kwargs)

        self.filters['make'].extra['choices'] = [
            (make.capitalize(), make.capitalize()) for make in Queries.uniqueMakes()
        ]

        self.filters['colour'].extra['choices'] = [
            (colour, colour) for colour in Queries.uniqueColours()
        ]
        


