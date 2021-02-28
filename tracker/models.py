from django.db import models
from profiles.models import Profile

class tracker(models.Model):
    profile = models.ForeignKeyField(Profile)
    ip_address = models.GenericIPAddressField()
    curr_page = models.CharField(max_length=20, null=True, blank=True)
    page_from  = models.CharField(max_length=20, null=True, blank=True)