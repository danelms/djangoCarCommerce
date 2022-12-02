import django_filters
from .models import Listing, Queries

class ListingFilter(django_filters.FilterSet):

    make = django_filters.ChoiceFilter(lookup_expr='iexact',empty_label="All makes")
    colour = django_filters.ChoiceFilter(lookup_expr='iexact',empty_label="All colours")
    mileage__lt = django_filters.NumberFilter(field_name='mileage', lookup_expr='lte',label="Maximum mileage") 
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte',label="Maximum price")
    ordering_filters = django_filters.OrderingFilter(label='Order results by', fields=['price', 'mileage', 'year'], empty_label="Most recently added")

    #Custom labels
    ordering_filters.field.choices=[
        ('price', 'Price - Highest to lowest'),
        ('-price', 'Price - Lowest to highest'),
        ('mileage', 'Mileage - Highest to lowest'),
        ('-mileage', 'Mileage - Lowest to highest'),
        ('year', 'Year - Newest to oldest'),
        ('-year', 'Year - Oldest to Newest'),
    ]

    class Meta:
        model = Listing
        fields = ['make', 'colour']

    def __init__(self, *args, **kwargs):
        super(ListingFilter, self).__init__(*args, **kwargs)

        self.filters['make'].extra['choices'] = [
            (make, make) for make in Queries.uniqueMakes()
        ]

        self.filters['colour'].extra['choices'] = [
            (colour, colour) for colour in Queries.uniqueColours()
        ]
        