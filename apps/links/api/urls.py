from django.urls import path
from apps.tags.api.views import (
                        TagView,
                        )


app_name = "links"


urlpatterns = [
    path('', TagView.as_view(), name='list'),
]