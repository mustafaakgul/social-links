from django.urls import path
from apps.tags.api.views import (
                        TagView,
                        )
from apps.links.api.views import (
                        GenericCustomLinkView,
                        ListCustomLinkView,
                        ListCreateCustomLinkView
                        )


app_name = "links"


urlpatterns = [
    path('tags', TagView.as_view(), name='list'),
    path('custom-links', GenericCustomLinkView.as_view(), name='custom-link-generics'),
    path('custom-links-generics', ListCreateCustomLinkView.as_view(), name='custom-link-generics'),
]