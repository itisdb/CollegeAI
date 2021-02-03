from templated_email import send_templated_mail

def generic_mailer():
    print("udit")
    send_templated_mail(
        template_name='welcome',
        from_email='bhardwaj.ud99@gmail.com',
        recipient_list=['hars.bhardwaj98@gmail.com'],
        context={
            'username':'Udit',
            'full_name':'Udit Bhardwaj',
            'signup_date':'11/12/2000'
        },create_link=True
    )

generic_mailer()