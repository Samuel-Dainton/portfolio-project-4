from django.test import TestCase
from .forms import RecipeForm, UserForm, Topic, Allergy


class TestRecipeForm(TestCase):

    # Tests to check required fields are not blank
    def setUp(self):

        topic_1 = Topic.objects.create(
        name='topic 1',
        )

        allergy_1 = Allergy.objects.create(
        name='nuts',
        )

    def test_recipe_title_is_required(self):
        form = RecipeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_recipe_method_is_required(self):
        form = RecipeForm({'method': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('method', form.errors.keys())
        self.assertEqual(
            form.errors['method'][0], 'This field is required.'
            )

    def test_recipe_ingredient_is_required(self):
        form = RecipeForm({'ingredient': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ingredient', form.errors.keys())
        self.assertEqual(
            form.errors['ingredient'][0], 'This field is required.'
            )

    # Test to check non required fields do not have to be present

    def test_non_required_fields_are_not_required(self):


        form = RecipeForm(
            {
                'title': 'Test', 'description': 'Test',
                'ingredient': ['Test'], 'method': 'Test',

                'topic': ['1'], 'allergy_info': ['1'],

                'prep_time': '1', 'cook_time': '1', 'author': 'Test',
                'difficulty': 'Easy', 'servings': '12'
                }
            )
        print(form.errors)
        self.assertTrue(form.is_valid())

# class TestCommentForm(TestCase):

#     # Test to check non required fields do not have to be present
    
#     def test_non_required_fields_are_not_required(self):

#         form = RecipeForm()
#         self.assertTrue(form.is_valid())