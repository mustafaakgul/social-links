from apps.tags.models import Tag
from rest_framework.generics import get_object_or_404, ListAPIView

from apps.tags.api.serializers import TagSerializer
from apps.links.api.serializers import SocialNetworkSerializer


class TagView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def get_queryset(self):
        return Tag.objects.filter(status=True)


class TagsNetworkView(ListAPIView):
    serializer_class = SocialNetworkSerializer

    def get_queryset(self):
        tag_id = self.kwargs['id']
        tag = get_object_or_404(Tag, id=tag_id)
        return tag.social_networks.all()