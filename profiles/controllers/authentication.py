from profiles.models import Profile


class RegistrationHandler:

    @staticmethod
    def send_registration_mail(profile_uuid):
        profile = Profile.objects.get(profile_uuid)
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )