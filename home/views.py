from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

def topic(request):
    return render(request, 'home/browse.html')

def home(request):
    q = request.GET.get('q')
    recipes = Recipe.objects.filter(topic__name=q)
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

