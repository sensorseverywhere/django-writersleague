from django.core import mail
from django.test import TestCase

from pages.forms import ContactForm


class TestContactForm(TestCase):
    def test_valid_contact_form(self):

        form = ContactForm(
            {
                "name":"user",
                "message":"message",
                "email":"user@email.com",
                "phone":"0982343534"
            }
        )

        assert form.is_valid()
