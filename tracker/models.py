from django.db import models
from profiles.models import Profile

class tracker(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    curr_page = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.ip_address