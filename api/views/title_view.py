from django.db.models import Avg
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.filters import TitleFilter
from api.models import Title
from api.permissions import AdminRequired, ReadOnly
from api.serializers import TitleDetailSerializer, TitleListSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('name')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TitleFilter
    permission_classes = [ReadOnly | AdminRequired]
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleListSerializer
        return TitleDetailSerializer
