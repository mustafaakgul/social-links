from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tags.models import Tag
from rest_framework.generics import get_object_or_404, ListCreateAPIView, ListAPIView

from apps.tags.api.serializers import TagSerializer
from apps.tags.api.pagination import TagPagination
from apps.links.api.serializers import SocialNetworkSerializer


class TagView(ListCreateAPIView):
    queryset = Tag.objects.all()
    permission_classes = []
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(status=True)


# class TagView(APIView):
#
#     def post(self, request):
#         try:
#             serializer = TagSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(
#                     {
#                         "status": "success",
#                         "message": "Tag created successfully",
#                         "errors": None,
#                         "data": serializer.data
#                     },
#                     status=status.HTTP_200_OK
#                 )
#             else:
#                 return Response(
#                     {
#                         "status": "error",
#                         "data": serializer.errors
#                     },
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#         except Exception as e:
#             return Response(
#                 {
#                     "status": "error",
#                     "message": "An error occurred",
#                     "errors": e.args,
#                     "data": str(e)
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def get(self, request, id=None):
#         if id:
#             item = Tag.objects.get(id=id, status=True)
#             serializer = TagSerializer(item)
#             return Response(
#                 {
#                     "status": "success",
#                     "data": serializer.data
#                 },
#                 status=status.HTTP_200_OK
#             )
#
#         items = Tag.objects.filter(status=True)
#         serializer = TagSerializer(items, many=True)
#         return Response(
#             {
#                 "status": "success",
#                 "data": serializer.data
#             },
#             status=status.HTTP_200_OK
#         )


# /list?q=12, tags/search?name=software
class TagQueryParamsView(ListAPIView):
    serializer_class = TagSerializer
    # pagination_class = TagPagination

    def get_queryset(self):
        queryset = Tag.objects.filter(status=True)
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class TagsNetworkView(ListAPIView):
    serializer_class = SocialNetworkSerializer

    def get_queryset(self):
        tag_id = self.kwargs['id']
        tag = get_object_or_404(Tag, id=tag_id)
        return tag.social_networks.all()