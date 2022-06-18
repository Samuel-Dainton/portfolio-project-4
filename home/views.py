from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm


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

    recipe_count = recipes.count()
    ingredient = Ingredient.objects.name

    context = {'recipes': recipes, 'recipe_count': recipe_count, 'ingredient': ingredient,}
    return render(request, 'home/index.html', context)


def recipe(request, title):
    recipe = Recipe.objects.get(title=title)
    context = {'recipe': recipe}
    return render(request, 'home/recipe.html', context)


@login_required
def createRecipe(request):

    form = RecipeForm()
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form, 'ingredient_form': IngredientForm()}
    return render(request, 'home/recipe_form.html', context)


@login_required()
def addIngredient(request):

    ingredient_form = IngredientForm()

    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient_form.save()
            return redirect('home')

    context = {'ingredient_form': ingredient_form}
    return render(request, 'home/recipe_form.html', context)


@login_required()
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


@login_required()
def deleteRecipe(request, title):
    recipe = Recipe.objects.get(title=title)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'home/delete.html', {'selected_object':recipe})

