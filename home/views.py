from django.shortcuts import render
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'home/index.html', context)

def recipe(request, title):
    recipe = Recipe.objects.get(title=title)
    return render(request, 'home/recipe.html')