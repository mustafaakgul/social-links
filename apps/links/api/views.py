from apps.tags.models import Tag
from apps.links.models import CustomLink
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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


# Class Based API Views
class ListCreateCustomLinkView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all custom links.
        """
        custom_links = CustomLink.objects.filter(user=self.request.user)
        serializer = CustomLinkSerializer(custom_links, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new custom link.
        """
        serializer = CustomLinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def custom_link_detail(request, pk):
    """
    Retrieve, update or delete a custom link.
    """
    custom_link = get_object_or_404(CustomLink, pk=pk)
    # OR
    # try:
    #     custom_link = CustomLink.objects.get(pk=pk)
    # except CustomLink.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CustomLinkSerializer(custom_link)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomLinkSerializer(custom_link, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # return Response(status=status.HTTP_204_NO_CONTENT
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        custom_link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)