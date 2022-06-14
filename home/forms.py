from django.forms import ModelForm
from .models import Recipe


# The form users see to create new recipes.
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        # Can also use ['title', 'servings', 'method' to exclude other fields]
        fields = ['title', 'servings', 'method', 'topic']
        