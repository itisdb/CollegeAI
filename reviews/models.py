from django.db import models

from base.models import BaseModel

from college.models import College

from profiles.models import Profile


class Review(BaseModel):

    class ReviewSources(models.IntegerChoices):
        GOOGLE = 1
        SHIKSHA = 2
        COLLEGE_DUNIA = 3
        COLLEGE_SEARCH = 4
        GET_MY_UNI = 5
        SELF = 6
        CAREER360 = 7
        OTHER = 0

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=200, null=True, blank=True)
    source = models.IntegerField(choices=ReviewSources.choices)
    batch = models.IntegerField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    is_displayed = models.BooleanField(default=True)
    quadrants = models.JSONField(null=True, blank=True)

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

'''
https://www.facebook.com/v3.2/dialog/oauth?client_id=187311743169596&

redirect_uri=https%3A%2F%2Fmycollegeai.com%2Fsocial-auth%2Fcomplete%2Ffacebook%2F
&state=bi9pYLvVAwhQ7ZoXAIlvJ2W0GxdO22Z1&return_scopes=true&ret=login&fbapp_pres=0&logger_id=a243128b-c0ca-4e8a-b444-636e0d1b8bc4&tp=unspecified&ext=1621866730&hash=AeZBDudkdpvUmWp6Y44
'''