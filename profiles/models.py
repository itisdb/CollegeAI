from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class Profile(BaseModel):
    """Profile class based on top of user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    display_pic = models.ImageField(upload_to='user/dp/', null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class OTPVerification(BaseModel):
    """OTP Verification stack trace."""

    class VerifierTag(models.IntegerChoices):
        """Reason for generating OTP."""
        MAIL_VERIFICATION = 1, _('MAIL VERIFICATION')
        PHONE_VERIFICATION = 2, _('PHONE VERIFICATION')
        PASSWORD_RESET = 3, _('PASSWORD RESET')
        OTHER = 0, _('Other')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    verifier_tag = models.IntegerField(choices=VerifierTag.choices)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.user.get_full_name()
