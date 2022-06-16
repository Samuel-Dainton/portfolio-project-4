from django.shortcuts import render
from .models import Recipe
from .forms import RecipeForm

def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'home/index.html', context)

def recipe(request, title):
    recipes = Recipe.objects.get(title=title)
    context = {'recipes': recipes}
    return render(request, 'home/recipe.html', context)

def createRecipe(request):

    form = RecipeForm()
    context = {'form': form}
    return render(request, 'home/recipe_form.html', context)