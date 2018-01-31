# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .views import show_credit
from django.core.urlresolvers import resolve
from django.conf import settings

class CreditPageTest(TestCase):
    def test_credit_page_resolves(self):
        credit_page = resolve('/credits')
        self.assertEqual(credit_page.func, show_credit)

class CardTest(TestCase):
   def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'tester1@testy.com',
            'password1': 'testpass',
            'password2': 'testpass',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 6,
            'expiry_year': 2021
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())        