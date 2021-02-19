from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class College(BaseModel):
    """Model for college."""

    class OwnershipChoices(models.IntegerChoices):
        """Choices for ownership."""
        PRIVATE = 0, _('Private')
        PUBLIC = 1, _('Public')
        OTHER = 2, _('Other')

    class InstitutionType(models.IntegerChoices):
        """Choices for Institution type."""
        GRADUATION_COLLEGE = 0,
        DIPLOMA_COLLEGE = 1,
        VOCATIONAL_TRAINING = 2

    class AssociatedMetrics(models.TextChoices):
        """Choices of metrics of each college."""
        OTHER = 'other'
        ACADEMIC = 'academic'
        INFRASTRUCTURE = 'infra'
        PLACEMENT = 'placement'

    full_name = models.CharField(null=True, max_length=255)
    abbreviated_name = models.CharField(null=True, max_length=50)
    meta_title = models.CharField(null=True, blank=True, max_length=500)
    meta = models.CharField(null=True, blank=True, max_length=500)
    keywords = models.CharField(null=True, blank=True, max_length=500)
    established_year = models.CharField(max_length=4, null=True, blank=True)
    city = models.CharField(null=True, max_length=50)
    state = models.CharField(null=True, max_length=50)
    image = models.ImageField(null=True, upload_to='college/image/')
    logo = models.ImageField(null=True, upload_to='college/logo/')
    ownership = models.IntegerField(null=True, choices=OwnershipChoices.choices)
    approval = models.CharField(null=True, max_length=100)
    college_type = models.IntegerField(null=True, choices=InstitutionType.choices)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    is_top = models.BooleanField(null=True, default=False)
    stream_degree = models.JSONField(null=True)
    entrance_exams = models.JSONField(null=True)
    website = models.CharField(max_length=400, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    scraping_urls = models.JSONField(null=True, blank=True)

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
