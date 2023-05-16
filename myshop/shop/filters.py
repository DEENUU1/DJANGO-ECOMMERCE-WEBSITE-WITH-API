import django_filters
from .models import Product, ProductRate, RATE


# This class allows to filter products on the main page
# It allows to filter by category and price
# User can choose prise less than and greater than


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "price": ["lt", "gt"],
            "category": ["exact"],
        }


# This class allows to filter product rates by date and rate


class RateFilter(django_filters.FilterSet):
    rate = django_filters.ChoiceFilter(choices=RATE, label="Filtruj opinie")

    class Meta:
        model = ProductRate
        fields = ["rate"]
