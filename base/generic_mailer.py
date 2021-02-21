from templated_email import send_templated_mail

def generic_mailer(**kwargs):
    send_templated_mail(
        template_name=kwargs.get('template_name'),
        from_email=settings.SMTP_EMAIL,
        recipient_list=kwargs.get('recipients'),
        username=kwargs.get('username'),
        full_name=kwargs.get('full_name'),
        create_link=True
    )