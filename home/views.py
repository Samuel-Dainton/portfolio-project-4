from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment, Allergy, UserProfile
from .forms import RecipeForm, UserForm
from django.contrib.auth.models import User

from django.core.paginator import Paginator
from django.shortcuts import render

def topic(request):
    return render(request, 'home/browse.html')

def home(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''


    if q:
        recipe_list = Recipe.objects.filter(
            Q(topic__name__icontains=q) |
            Q(title__icontains=q)  |
            Q(ingredient__icontains=q)
    )
    else:
        recipe_list = Recipe.objects.all()


    mylist = recipe_list.distinct()

    recipe_counter = Recipe.objects.all()
    recipe_count = recipe_counter.count()

    paginator = Paginator(mylist, 12) # Show 12 recipes per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'mylist': mylist, 'recipe_count': recipe_count, 'page_obj': page_obj}
    return render(request, 'home/index.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    recipes = user.recipe_set.all()

    paginator = Paginator(recipes, 12) # Show 12 recipes per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'user': user, 'recipes': recipes, 'page_obj': page_obj}
    return render(request, 'home/profile.html', context)


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
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/recipe_form.html', context)

@login_required()
def updateRecipe(request, title):

    recipe = Recipe.objects.get(title=title)
    form = RecipeForm(instance=recipe)
    
    if request.user != recipe.author:
        return HttpResponse('This is not your recipe to edit.')

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/recipe_form.html', context)


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

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            print(form)
            print(form.data)
            return redirect('user-profile', pk=user.id)
    context = {'form': form}
    return render(request, 'home/update-user.html', context)