from django.core.mail import send_mail
from django.conf import settings
# Send Mail 
def sending():
    subject="This is a try version"
    msg="NIce tomeet you"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["sami606715@gmail.com"]

    send_mail(subject,msg,from_email,recipient_list)
