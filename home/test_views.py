from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment


class TestViews(TestCase):

    def setUp(self):
        self.test_user = User.objects.create(
            password='abc123', username='testuser'
            )

    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    # Default get keeps returning 301, follow leads to extention templates.
    def test_get_create_recipe_page(self):
        response = self.client.get('/create-recipe')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/recipe_form.html')