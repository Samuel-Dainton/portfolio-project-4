from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('browse/', views.topic, name="browse"),

    path('recipe/<str:title>', views.recipe, name="recipe"),
    path('create-recipe/', views.createRecipe, name='create-recipe'),
    path('update-recipe/<str:title>', views.updateRecipe, name='update-recipe'),
    path('delete-recipe/<str:title>', views.deleteRecipe, name='delete-recipe'),
    path('delete-comment/<str:pk>', views.deleteComment, name='delete-comment'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('update-user/', views.updateUser, name='update-user'),
]