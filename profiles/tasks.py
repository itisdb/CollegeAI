from celery import shared_task

from profiles.controllers.authentication import RegistrationHandler


@shared_task
def send_registration_mail_task(profile_uuid):
    RegistrationHandler().send_registration_mail(profile_uuid)
