from django.conf import settings
from templated_email import send_templated_mail


def generic_mailer(**kwargs):
    if kwargs.get('link'):
        link = kwargs.get('link')
    else:
        link = 'https://mycollegeai.com/'
    send_templated_mail(
        template_name=kwargs.get('template_name'),
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=kwargs.get('recipients'),
        context = {
        'username': kwargs.get('username'),
        'full_name' : kwargs.get('first_name'),
        'link' : link,
        },
        create_link=True

    )