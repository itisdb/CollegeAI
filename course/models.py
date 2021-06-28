from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


# Create your models here.
class Course(BaseModel):
    full_name = models.CharField(null=True, max_length=255)
    abbreviated_name = models.CharField(null=True, max_length=50)
    meta_title = models.CharField(null=True, blank=True, max_length=500)
    meta = models.TextField(null=True, blank=True)
    meta_keywords = models.JSONField(null=True, blank=True, default={})
    about = models.TextField(null=True, blank=True)
    stream = models.CharField(null=True, max_length=255)
    level = models.CharField(null=True, max_length=255)
    duration = models.CharField(null=True, max_length=255)
    examination_type = models.CharField(null=True, max_length=255)
    avg_course_fees = models.CharField(null=True, max_length=255)
    eligibility = models.TextField(null=True)
    syllabus = models.JSONField(null=True)
    career = models.JSONField(null=True)
    top_institutes = models.JSONField(null=True)
    slug = models.SlugField(null=True, blank=True, max_length=100)
    is_top = models.BooleanField(null=True, default=False)

    

    def __str__(self):
        return '{}'.format(self.abbreviated_name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super(Course, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)
