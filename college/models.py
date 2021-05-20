from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel
from profiles.models import Profile


class CollegeFacilities(BaseModel):

    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class College(BaseModel):
    """Model for college."""

    class OwnershipChoices(models.IntegerChoices):
        """Choices for ownership."""
        PRIVATE = 0, _('Private')
        PUBLIC = 1, _('Public')
        OTHER = 2, _('Other')

    class AssociatedMetrics(models.TextChoices):
        """Choices of metrics of each college."""
        OTHER = 'other'
        ACADEMIC = 'academic'
        INFRASTRUCTURE = 'infra'
        PLACEMENT = 'placement'

    full_name = models.CharField(null=True, max_length=255)
    abbreviated_name = models.CharField(null=True, max_length=50)
    meta_title = models.CharField(null=True, blank=True, max_length=500)
    meta = models.TextField(null=True, blank=True)
    meta_keywords = models.JSONField(null=True, blank=True, default=[])
    about_us = models.JSONField(null=True, blank=True)
    established_year = models.CharField(max_length=4, null=True, blank=True)
    city = models.CharField(null=True, max_length=50)
    state = models.CharField(null=True, max_length=50)
    image = models.ImageField(null=True, upload_to='college/image/')
    logo = models.ImageField(null=True, upload_to='college/logo/')
    ownership = models.IntegerField(null=True, choices=OwnershipChoices.choices)
    approval = models.CharField(null=True, max_length=100)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    is_top = models.BooleanField(null=True, default=False)
    degree = models.JSONField(null=True)
    stream_degree = models.JSONField(null=True)
    entrance_exams = models.CharField(null=True, max_length=200)
    website = models.CharField(max_length=400, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    scraping_urls = models.JSONField(null=True, blank=True)
    facilities = models.ManyToManyField(CollegeFacilities)

    def __str__(self):
        return '{}, {}'.format(self.abbreviated_name, self.city)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super(College, self).save(*args, **kwargs)


class CollegeImages(BaseModel):

    image = models.ImageField(upload_to='college/gallery/')
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.college.full_name


class CollegeBookmark(BaseModel):

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username} bookmarked {self.college.abbreviated_name}'

    class Meta:
        unique_together = ('college', 'profile', )
