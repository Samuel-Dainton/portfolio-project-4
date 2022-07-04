from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment


class TestViews(TestCase):

    def setUp(self):
        self.test_user = User.objects.create(
            password='abc123', username='testuser'
            )

        self.recipe = Recipe.objects.create(title='Test', author=self.test_user)
        self.vegan_recipe = Recipe.objects.create(
            title='Onion Gravy',
            author= self.test_user
            )
        self.vegetarian_recipe = Recipe.objects.create(
            title='Salad',
            author= self.test_user
            )

        self.comment = Comment.objects.create(
            body='Test Comment', recipe=self.recipe, user=self.test_user
            )
        self.client.login(username='testuser', password='abc123')

    def test_user_pw(self):
        checked = self.test_user.check_password('abc123')
        self.assertTrue(checked)

    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    # Default get keeps returning 301, follow leads to extention templates.
    def test_get_create_recipe_page(self):
        response = self.client.get('/create-recipe', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/recipe_form.html')