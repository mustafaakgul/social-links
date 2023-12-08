from rest_framework.serializers import ModelSerializer

from apps.links.models import SocialNetwork, CustomLink


class SocialNetworkSerializer(ModelSerializer):

    class Meta:
        model = SocialNetwork
        fields = (
            'id',
            'network',
            'base_url',
        )


class CustomLinkSerializer(ModelSerializer):

    class Meta:
        model = CustomLink
        fields = (
            'id',
            'title',
            'url',
        )
