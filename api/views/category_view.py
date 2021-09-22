from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from api.mixins import CreateListDeleteViewSet
from api.models import Category
from api.permissions import AdminRequired, ReadOnly
from api.serializers import CategorySerializer


class CategoryViewSet(CreateListDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [ReadOnly | AdminRequired]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    pagination_class = PageNumberPagination
