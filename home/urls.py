from . import views
from django.urls import path


urlpatterns = [
    path("", views.RecipeList.as_view(), name='home'),

    path('create-recipe/', views.CreateRecipe.as_view(), name="create-recipe"),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name='recipe_detail'),
]