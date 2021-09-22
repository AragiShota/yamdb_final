from rest_framework import serializers

from api.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    def validate(self, data):
        user = self.context['request'].user
        title_id = self.context['view'].kwargs['title_id']
        review = user.reviews.filter(title_id=title_id)
        method = self.context['request'].method
        if review.count() != 0 and method == 'POST':
            raise serializers.ValidationError(
                f'Only one review must be to title with id:{title_id}'
            )
        return data

    class Meta:
        model = Review
        exclude = ['title']
