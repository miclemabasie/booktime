from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)

    message = forms.CharField(widget=forms.Textarea, max_length=600)

    def clean_name(self):
        name = self.cleaned_data["name"]
        print(f"#################{name}")
        if name == "miclem":
            raise forms.ValidationError("The name can not set to miclem.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get("message")
        return message

    def send_mail(self):
        logger.info(f"Sending Email to")
        # message = f"From: {name}"
        print("Testing the sendmail function")
        send_mail(
            "Site Message",
            "message",
            "miclemabasie@mail.com",
            ["booktim@site.com"],
        )
