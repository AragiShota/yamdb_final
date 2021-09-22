from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from api.mixins import CreateListDeleteViewSet
from api.models import Genre
from api.permissions import AdminRequired, ReadOnly
from api.serializers import GenreSerializer


class GenreViewSet(CreateListDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [ReadOnly | AdminRequired]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    pagination_class = PageNumberPagination
