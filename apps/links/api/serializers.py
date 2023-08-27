from rest_framework.serializers import ModelSerializer

from apps.links.models import SocialNetwork


class SocialNetworkSerializer(ModelSerializer):

    class Meta:
        model = SocialNetwork
        fields = (
            'id',
            'network',
            'base_url',
        )
