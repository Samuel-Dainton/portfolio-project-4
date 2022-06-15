from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def recipe(request):
    return render(request, 'recipe.html')