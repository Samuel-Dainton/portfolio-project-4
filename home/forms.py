from django.forms import ModelForm
from .models import Recipe, Ingredient, Comment

class RecipeForm(ModelForm):
    class Meta: 
        model = Recipe
        # Can use ['name', 'method'...] to select specific values.
        fields = '__all__'
        exclude = ['author',]

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        exclude = ['recipe',]
        recipe = Recipe.title

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('body',)