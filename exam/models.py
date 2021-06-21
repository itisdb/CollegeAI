from django.db import models
from django.utils.text import slugify
from django.utils.translation import TranslatorCommentWarning, gettext_lazy as _

from base.models import BaseModel
# Create your models here.

class Exam(BaseModel):
    full_name = models.CharField(null=True, max_length=255)
    abbreviated_name = models.CharField(null=True, max_length=50)
    meta_title = models.CharField(null=True, blank=True, max_length=500)
    meta = models.TextField(null=True, blank=True)
    exam_level = models.CharField(null=True, max_length=150)
    conducting_body = models.CharField(null=True, max_length=255)
    website = models.CharField(null=True, max_length=255)
    tentative_date = models.CharField(null=True, max_length=100)
    basic_eligibility = models.CharField(null=True, max_length=100)
    about = models.TextField(null=True)
    important_detais = models.JSONField(null=True)
    cutoff = models.JSONField(null = True)
    eligibility = models.TextField(null=True)
    application_form = models.TextField(null=True)
    slug = models.SlugField(null=True, blank=True, max_length=100)
    is_top = models.BooleanField(null=True, default=False)

    def __str__(self):
        return '{}'.format(self.abbreviated_name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super(Exam, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)
