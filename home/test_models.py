from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment, Recipe


class TestModels(TestCase):

    def setUp(self):
        self.test_user = User.objects.create(
            password='abc123', username='testuser'
            )

    def test_recipe_model_str(self):

        recipe = Recipe.objects.create(title='Test Recipe')
        self.assertEqual(str(recipe.title), 'Test Recipe')

    def test_recipe_model_int(self):

        recipe = Recipe.objects.create(prep_time=10)
        self.assertEqual(int(recipe.prep_time), 10)

    def test_comment_model_str(self):

        recipe = Recipe.objects.create(title='Test Recipe')
        comment = Comment.objects.create(
            body='Comment Test by test_user',
            recipe=recipe,
            user=self.test_user
            )
        self.assertEqual(str(comment), 'Comment Test by test_user')