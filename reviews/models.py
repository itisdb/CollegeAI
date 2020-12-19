from django.db import models

from base.models import BaseModel
from college.models import College


class Reviews(BaseModel):

    class ReviewSources(models.IntegerChoices):
        GOOGLE = 1
        SHIKSHA = 2
        COLLEGE_DUNIA = 3
        COLLEGE_SEARCH = 4
        GET_MY_UNI = 5
        OTHER = 0

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(null=True, blank=True)
    source = models.IntegerField(choices=ReviewSources.choices)
    batch = models.IntegerField(null=True)

    def __str__(self):
        return self.comment


class Rating(BaseModel):

    college = models.OneToOneField(College, on_delete=models.CASCADE)
    overall = models.FloatField(null=True, blank=True)
    infrastructure = models.FloatField(null=True, blank=True)
    placement = models.FloatField(null=True, blank=True)
    academics = models.FloatField(null=True, blank=True)
    value_for_money = models.FloatField(null=True, blank=True)
    campus_life = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.college.full_name
