from celery import shared_task


@shared_task
def send_registration_mail(profile_uuid):
    return profile_uuid
