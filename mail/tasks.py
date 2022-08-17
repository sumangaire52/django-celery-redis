from time import sleep

from celery import shared_task

from django.core.mail import send_mail


@shared_task()
def send_email_task(email, message):
    sleep(20)
    send_mail(
        "Mail Received",
        message,
        'mail@sample.com',
        [email],
        fail_silently=False)