from apps.tags.models import Tag
from rest_framework.generics import get_object_or_404, ListAPIView

from apps.tags.api.serializers import TagSerializer


class TagView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    ordering_fields = ['created_at']

    def get_queryset(self):
        return Tag.objects.filter(status=True)
