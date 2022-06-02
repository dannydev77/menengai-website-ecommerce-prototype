
from django.db.models.query import QuerySet
import django_filters
from django_filters import CharFilter


from .models import *
class ProductFilterForm(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    
    # price = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all())#widgets = forms.CheckboxSelectMultiple)
    class Meta:
        model = Product
        fields = ['name']

        