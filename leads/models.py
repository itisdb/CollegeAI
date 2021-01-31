from django.db import models

from base.models import BaseModel


class DirectLead(BaseModel):
    """Store all direct leads from any public form."""

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    extras = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
