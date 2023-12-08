from django.urls import path
from apps.tags.api.views import (
                        TagView,
                        )
from apps.links.api.views import (
                        ListCustomLinkView,
                        )


app_name = "links"


urlpatterns = [
    path('tags', TagView.as_view(), name='list'),
    path('custom-links', ListCustomLinkView.as_view(), name='custom-link-list'),
]