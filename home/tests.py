from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Recipe, Ingredient

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')

    def test_user_pw(self):
        checked = self.user_a.check_password("abc123")
        self.assertTrue(checked)