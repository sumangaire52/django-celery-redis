from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from .forms import SendMailForm


class SendMailView(FormView):
    form_class = SendMailForm
    template_name = 'mail/send_email_form.html'
    success_url = 'success'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'mail/success.html'