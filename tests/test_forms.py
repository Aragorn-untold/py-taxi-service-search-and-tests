from django.test import TestCase

from taxi.forms import DriverCreationForm


class FormsTests(TestCase):
    def test_driver_creation_form(self):
        form_data = {
            "username": "Name",
            "password1": "Test1234!@#",
            "password2": "Test1234!@#",
            "license_number": "ASD12345",
            "first_name": "Test",
            "last_name": "Testovich"
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data, form_data)
