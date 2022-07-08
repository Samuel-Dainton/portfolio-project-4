from django import forms
from django.forms import ModelForm
from .models import Recipe, Topic, Allergy, UserProfile
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget

class RecipeForm(forms.ModelForm):
    
    ingredient = forms.CharField(widget=SummernoteWidget())
    introduction = forms.CharField(widget=SummernoteWidget())
    method = forms.CharField(widget=SummernoteWidget())
    class Meta: 
        model = Recipe
        # Can use ['name', 'method'...] to select specific values.
        fields = '__all__'
        exclude = ['author']

    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    allergy_info = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']