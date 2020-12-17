from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class College(models.Model):
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

    full_name = models.CharField(null=True, max_length=255)
    abbreviated_name = models.CharField(null=True, max_length=50)
    meta = models.TextField(null=True)
    keywords = models.TextField(null=True)
    city = models.CharField(null=True, max_length=50)
    state = models.CharField(null=True, max_length=50)
    brochure = models.FileField(null=True, upload_to='college/brochure/')
    image = models.ImageField(null=True, upload_to='college/image/')
    logo = models.ImageField(null=True, upload_to='college/logo/')
    ownership = models.IntegerField(null=True, choices=OwnershipChoices.choices)
    approval = models.CharField(null=True, max_length=100)
    college_type = models.IntegerField(null=True, choices=InstitutionType.choices)
    established_year = models.CharField(null=True, max_length=100)
    slug = models.SlugField(null=True, max_length=50)
    about = models.TextField(null=True)
    is_top = models.BooleanField(null=True, default=False)
    admission_process = models.TextField(null=True)
    placements = models.TextField(null=True)
    degrees = models.JSONField(null=True) #CSV field
    stream_degree = models.JSONField(null=True) #CSV field
    streams = models.JSONField(null=True) #CSV field
    entrance_exams = models.JSONField(null=True) #CSV field
    contacts = models.JSONField(null=True) #CSV field
    images = models.JSONField(null=True) #CSV field

    def __str__(self):
        return '{}, {}'.format(self.abbreviated_name, self.city)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super(College, self).save(*args, **kwargs)
