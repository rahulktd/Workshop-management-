import django_filters
from django import forms
from django.db.models import Q

from service.models import Login


class WorkerFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(field_name='name',label='',lookup_expr='icontains',widget=forms.TextInput(attrs={'class':'form-control'}))
    # class Meta:
    #     model = Login
    #     fields = ('name','mobile',)

    search = django_filters.CharFilter(method='search_filter', label='Search',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Login
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(mobile__icontains=value) |
            Q(email__icontains=value) |
            Q(address=value)
        )

class CustomerFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(field_name='name',label='',lookup_expr='icontains',widget=forms.TextInput(attrs={'class':'form-control'}))
    # class Meta:
    #     model = Login
    #     fields = ('name',)

    search = django_filters.CharFilter(method='search_filter', label='Search',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Login
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(mobile__icontains=value) |
            Q(email__icontains=value) |
            Q(address=value)
        )

