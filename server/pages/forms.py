import logging

from django import forms
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(label='First Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone = forms.CharField(label='Phone', max_length=12)
    message = forms.CharField(widget=forms.Textarea)

    def send_mail(self):

        message = "From {0}\n{1}\n{2}\n{3}".format(
            self.cleaned_data["name"],
            self.cleaned_data["message"],
            self.cleaned_data["email"],
            self.cleaned_data["phone"],   
        )
        
        email = "d-pkg <{0}>".format(self.cleaned_data["email"])

        send_mail(
                  "d-pkg Contact", 
                  message,
                  "d-pkg <wade@d-pkg.com",
                  ["wade_mansell@hotmail.com"]
                  )
