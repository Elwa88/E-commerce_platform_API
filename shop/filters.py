import django_filters
from .models import Product

class ProductFilters(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category','name']