from django.urls import path
from apps.tags.api.views import (
                        TagView,
                        TagsNetworkView,
                        )


app_name = "tags"


urlpatterns = [
    path('', TagView.as_view(), name='list'),
    path('<int:id>/networks', TagsNetworkView.as_view(), name='tags_networks'),
]