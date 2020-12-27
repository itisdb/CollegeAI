import random

from django.core.mail import send_mail

from profiles.models import OTPVerification, Profile


class RegistrationHandler:

    @staticmethod
    def send_registration_mail(profile_uuid):
        profile = Profile.objects.get(profile_uuid)
        otp_object = OTPVerification.objects.get_or_create(
            profile=profile,
            otp=str(random.randint(100000, 999999)),
            verifier_tag=OTPVerification.VerifierTag.MAIL_VERIFICATION.value,
            is_verified=False
        )
        send_mail(
            'Complete your Registration - MyCollegeAI',
            'Thank you for registering. Please complete the registration by using this OTP: {}'.format(
                otp_object.otp
            ),
            'admin@mycollegeai.com',
            [profile.user.email],
            fail_silently=False,
        )

    @staticmethod
    def validate_mail_otp(user, otp):
        profile = user.profile
        try:
            otp_object = OTPVerification.objects.get(
                profile=profile,
                otp=otp,
                verifier_tag=OTPVerification.VerifierTag.MAIL_VERIFICATION.value,
                is_verified=False
            )
            otp_object.is_verified = True
            otp_object.save()
            return True
        except BaseException:
            return False
