from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment, Allergy, UserProfile, Like
from .forms import RecipeForm, UserForm
from django.contrib.auth.models import User

from django.core.paginator import Paginator
from django.shortcuts import render

def topic(request):
    return render(request, 'home/browse.html')

def home(request):
    
    # Search Function
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if q:
        recipe_list = Recipe.objects.filter(
            Q(topic__name__icontains=q) |
            Q(title__icontains=q)  |
            Q(ingredient__icontains=q)
    )
    else:
        recipe_list = Recipe.objects.all()

    # Checks that only one instance of each recipe is returned
    mylist = recipe_list.distinct()

    # Recipe counter
    recipe_counter = Recipe.objects.all()
    recipe_count = recipe_counter.count()

    # Paginator, 12 recipes per page
    paginator = Paginator(mylist, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'mylist': mylist, 'recipe_count': recipe_count, 'page_obj': page_obj}
    return render(request, 'home/index.html', context)


def userProfile(request, pk):

    user = get_object_or_404(User, id=pk)
    recipes = user.recipe_set.all()

    paginator = Paginator(recipes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'user': user, 'recipes': recipes, 'page_obj': page_obj}
    return render(request, 'home/profile.html', context)


def recipe(request, title):

    recipe = get_object_or_404(Recipe, title=title)
    comments = recipe.comment_set.all().order_by('-created')
    
    # Comment post method
    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            recipe = recipe,
            body = request.POST.get('body')
        )
        return redirect('recipe', title=recipe.title)

    liked_list = recipe.liked.all()

    context = {'recipe': recipe, 'comments':comments, 'liked_list': liked_list}
    return render(request, 'home/recipe.html', context)

def likeRecipe(request):

    user = request.user

    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        recipe_obj = Recipe.objects.get(id=recipe_id)

        if user in recipe_obj.liked.all():
            recipe_obj.liked.remove(user.id)
        else:
            recipe_obj.liked.add(user.id)
        like, created = Like.objects.get_or_create(user=user, recipe_id=recipe_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect(reverse('recipe', kwargs={'title':recipe_obj}))

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

    recipe = get_object_or_404(Recipe, title=title)
    form = RecipeForm(instance=recipe)
    
    # Checks that user is the author incase unothorised user accesses the page
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

    recipe = get_object_or_404(Recipe, title=title)

    if request.user != recipe.author:
        return HttpResponse('This is not your recipe to delete.')

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'home/delete.html', {'selected_object': recipe})

@login_required()
def deleteComment(request, pk, recipe):
    
    comment = get_object_or_404(Comment, id=pk)
    recipe_obj = get_object_or_404(Recipe, title=recipe)

    if request.user != comment.user:
        return HttpResponse('This is not your comment to delete.')

    # Delete function returns the user back to the recipe page they came from
    if request.method == 'POST':
        comment.delete()
        return redirect(reverse('recipe', kwargs={'title':recipe_obj}))

    return render(request, 'home/delete.html', {'selected_object': comment})

@login_required(login_url='login')
def updateUser(request):

    userprofile = request.user.userprofile
    form = UserForm(instance=userprofile)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save()
            print(form)
            print(form.data)
            return redirect('user-profile', pk=request.user.id)

    context = {'form': form}
    return render(request, 'home/update_user.html', context)

def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response