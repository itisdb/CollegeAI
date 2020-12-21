from django.contrib import admin

from reviews.models import Rating, Review

admin.site.register(Review)
admin.site.register(Rating)
