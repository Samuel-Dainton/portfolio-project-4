from django.shortcuts import render

def home(request):
    context = {'recipes': recipes}
    return render(request, 'home/index.html', context)

def recipe(request, title):
    return render(request, 'home/recipe.html')