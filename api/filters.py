from django_filters import rest_framework as filters

from api.models import Title


class TitleFilter(filters.FilterSet):
    category = filters.CharFilter(
        field_name='category__slug',
        lookup_expr='iexact'
    )
    genre = filters.CharFilter(field_name='genre__slug', lookup_expr='iexact')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ['category', 'name', 'year', 'genre']
