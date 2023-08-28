from django.urls import path
from apps.tags.api.views import (
                        TagView,
                        TagQueryParamsView,
                        TagsNetworkView,
                        )


app_name = "tags"


urlpatterns = [
    path('', TagView.as_view(), name='list'),
    path('search', TagQueryParamsView.as_view(), name='list_query_params'),
    path('<int:id>/networks', TagsNetworkView.as_view(), name='tags_networks'),
]