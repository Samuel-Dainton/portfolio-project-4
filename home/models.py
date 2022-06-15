from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Units(models.Model):
    unit = models.CharField(max_length=200)

    def __str__(self):
        return self.unit

class Ingredients(models.Model):
    quantity = models.CharField(max_length=10)
    ingredient = models.Charfield(max_length=50)
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True)

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ManyToMany(Topic, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, default="recipe_image.png")
    prep_time = models.Charfield(max_length=50)
    cook_time = models.Charfield(max_length=50)
    difficulty = models.CharField(max_length=50)
    servings = models.CharField(max_length=50)
    introduction = RichTextField(blank=True, null=True)
    method = RichTextField(blank=True, null=True)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.SET_NULL, null=True)
    calories = models.CharField(max_length=50)
    fat = models.CharField(max_length=50)
    carbs =models.CharField(max_length=50)
    protein = models.CharField(max_length=50)
    allergy_info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
    ordering = ['-created']

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

