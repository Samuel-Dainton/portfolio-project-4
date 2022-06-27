from django import forms
from django.forms import ModelForm
from .models import Recipe, Comment, Topic, Allergy

class RecipeForm(forms.ModelForm):
    class Meta: 
        model = Recipe
        # Can use ['name', 'method'...] to select specific values.
        fields = '__all__'
        exclude = ['author',]
        
    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    allergy_info = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
