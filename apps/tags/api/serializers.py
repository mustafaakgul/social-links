from rest_framework.serializers import ModelSerializer

from apps.tags.models import Tag


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'status',
        )
