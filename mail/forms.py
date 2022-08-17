from django import forms 
from .tasks import send_email_task


class SendMailForm(forms.Form):
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.TextInput)

    def send_email(self):
        send_email_task.delay(self.cleaned_data['email'],self.cleaned_data['message'])