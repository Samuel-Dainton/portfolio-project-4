from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.forms.models import modelformset_factory

from .models import Recipe, Ingredient, Comment
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
    comments = recipe.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            recipe = recipe,
            body = request.POST.get('body')
        )
        return redirect('recipe', title=recipe.title)

    context = {'recipe': recipe, 'comments':comments}
    return render(request, 'home/recipe.html', context)


@login_required
def createRecipe(request):

    form = RecipeForm()
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')

    context = {'form': form, 'ingredient_form': IngredientForm()}
    return render(request, 'home/recipe_form.html', context)


@login_required()
def updateRecipe(request, title):

    obj = get_object_or_404(Recipe, title=title, author=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    # form_2 = IngredientForm(request.POST or None)
    
    IngredientFormset = modelformset_factory(Ingredient, form=IngredientForm, extra=0)
    qs = obj.ingredient_set.all()
    formset = IngredientFormset(request.POST or None, queryset=qs)
    context = {'form': form, 'formset': formset, 'object': obj}
    
    if request.method == 'POST':
        if all([form.is_valid(), formset.is_valid()]):
            parent = form.save(commit=False)
            parent.save()
            for form in formset:
                child = form.save(commit=False)
                child.recipe = parent
                child.save()

            context['message'] = 'Recipe Updated'

    return render(request, "home/recipe_form.html", context)


@login_required()
def deleteRecipe(request, title):
    recipe = Recipe.objects.get(title=title)

    if request.user != recipe.author:
        return HttpResponse('This is not your recipe to delete.')

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'home/delete.html', {'selected_object': recipe})

@login_required()
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse('This is not your recipe to delete.')

    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'home/delete.html', {'selected_object': comment})

