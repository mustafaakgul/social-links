from django.db import models

from apps.common.models import CoreModel


class Tag(CoreModel):
    name = models.CharField(max_length=35)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name
