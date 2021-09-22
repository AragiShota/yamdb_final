from rest_framework import serializers, validators

from api.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(validators=[validators.UniqueValidator(
        queryset=Genre.objects.all())])

    class Meta:
        model = Genre
        exclude = ('id',)
