from rest_framework import serializers, validators

from api.models import Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(validators=[validators.UniqueValidator(
        queryset=Category.objects.all())])

    class Meta:
        model = Category
        exclude = ('id',)
