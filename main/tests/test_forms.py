from django.test import TestCase
from django.core import mail
from main import forms


class TestForm(TestCase):
    def test_contact_form_works(self):
        form = forms.ContactForm(
            {
                "name": "miclem",
                "message": "This is a test message",
            }
        )

        self.assertTrue(form.is_valid())
        with self.assertLogs("main.forms", level="INFO") as cm:
            form.send_mail()

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Site Message")

        self.assertGreaterEqual(len(cm.output), 1)

    def test_invalid_contact_form(self):
        form = forms.ContactForm(
            {
                "message": "This is a faild form because the name is not available",
            }
        )

        self.assertFalse(form.is_valid())
