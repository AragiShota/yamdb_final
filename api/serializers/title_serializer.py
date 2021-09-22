from rest_framework import serializers

from api.models import Category, Genre, Title
from api.serializers import CategorySerializer, GenreSerializer


class TitleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class TitleDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    category = serializers.SlugRelatedField(
        slug_field='slug',
        required=False,
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        required=False,
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Title
        fields = '__all__'
