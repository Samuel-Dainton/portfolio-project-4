from django import forms
from django.forms import ModelForm
from .models import Recipe, Comment, Topic

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
