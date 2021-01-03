import random

from django.core.mail import EmailMessage

from profiles.models import OTPVerification, Profile


class RegistrationHandler:

    @staticmethod
    def send_registration_mail(profile_uuid):
        profile = Profile.objects.get(uuid=profile_uuid)
        otp_object, _ = OTPVerification.objects.get_or_create(
            profile=profile,
            otp=str(random.randint(100000, 999999)),
            verifier_tag=OTPVerification.VerifierTag.MAIL_VERIFICATION.value,
            is_verified=False
        )
        email = EmailMessage(
            'Complete your Registration - MyCollegeAI',
            'Thank you for registering. Please complete the registration by using this OTP: {}'.format(
                otp_object.otp
            ),
            'admin@mycollegeai.com',
            [profile.user.email],
            ['sonicxxx7@gmail.com'],
            reply_to=['admin@mycollegeai.com']
        )
        email.content_subtype = "html"
        email.send(fail_silently=True)

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
