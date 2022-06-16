from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta: 
        model = Recipe
        # Can use ['name', 'method'...] to select specific values.
        fields = '__all__'