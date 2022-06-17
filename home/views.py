from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Recipe
from .forms import RecipeForm


def topic(request):
    return render(request, 'home/browse.html')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    recipes = Recipe.objects.filter(
        Q(topic__name__icontains=q) |
        Q(title__icontains=q) 
        # TODO search comes from recipe but ingredients is not in recipe. (Don't forget to add | for or)
        # Q(ingredient__icontains=q)
    )

    context = {'recipes': recipes}
    return render(request, 'home/index.html', context)


def recipe(request, title):
    recipes = Recipe.objects.get(title=title)
    context = {'recipes': recipes}
    return render(request, 'home/recipe.html', context)

def createRecipe(request):

    form = RecipeForm()
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/recipe_form.html', context)

def updateRecipe(request, title):

    recipe = Recipe.objects.get(title=title)
    form = RecipeForm(instance=recipe)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/recipe_form.html', context)

def deleteRecipe(request, title):
    recipe = Recipe.objects.get(title=title)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'home/delete.html', {'selected_object':recipe})

