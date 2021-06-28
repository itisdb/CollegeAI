from django.contrib import admin

from college.models import College, CollegeImages, CollegeFacilities, CollegeGenres


class CollegeImageInline(admin.StackedInline):
    model = CollegeImages


class CollegeAdmin(admin.ModelAdmin):
    inlines = [CollegeImageInline]
    filter_horizontal = ('facilities','tags',)
    model = College


admin.site.register(College, CollegeAdmin)
admin.site.register(CollegeFacilities)
admin.site.register(CollegeGenres)