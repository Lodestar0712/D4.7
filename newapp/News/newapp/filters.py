from django_filters import FilterSet, DateFilter
from .models import *
import django.forms

class PostFilter(FilterSet):
    class Meta:
        model =Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['exact'],
            'text':['icontains'],
            'postCategory':['exact']
        }
    dateCreation = DateFilter(
        lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )
