from django import forms
from django.forms import ModelForm
from .models import Recipe, Ingredient, Comment, Topic

class RecipeForm(forms.ModelForm):
    class Meta: 
        model = Recipe
        # Can use ['name', 'method'...] to select specific values.
        fields = '__all__'
        exclude = ['author',]
        
    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

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