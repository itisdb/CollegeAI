from django.contrib import admin

from profiles.models import Profile, OTPVerification, psychometry

admin.site.register(Profile)
admin.site.register(OTPVerification)
admin.site.register(psychometry)