from apps.tags.models import Tag
from apps.links.models import CustomLink
from rest_framework.generics import get_object_or_404, ListAPIView

from apps.tags.api.serializers import TagSerializer
from apps.links.api.serializers import CustomLinkSerializer


class TagView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    ordering_fields = ['created_at']

    def get_queryset(self):
        return Tag.objects.filter(status=True)


class ListCustomLinkView(ListAPIView):
    serializer_class = CustomLinkSerializer
    queryset = CustomLink.objects.all()
    ordering_fields = ['created_at']

    def get_queryset(self):
        return CustomLink.objects.filter(user=self.request.user)
