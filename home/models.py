from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image', null=True, default="recipe_image.png")
    bio = models.TextField(null=True)

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
    ingredient = models.CharField(max_length=50)
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True)

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ManyToManyField(Topic,)
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', null=True, default="recipe_image.png")
    prep_time = models.CharField(blank=True, max_length=50)
    cook_time = models.CharField(blank=True, max_length=50)
    difficulty = models.CharField(max_length=50)
    servings = models.CharField(max_length=50)
    introduction = RichTextField(blank=True, null=True)
    method = RichTextField(blank=True, null=True)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.SET_NULL, null=True)
    calories = models.CharField(blank=True, max_length=50)
    fat = models.CharField(blank=True, max_length=50)
    carbs =models.CharField(blank=True, max_length=50)
    protein = models.CharField(blank=True, max_length=50)
    allergy_info = models.TextField(blank=True, )
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
        ordering = ['-created']

    def __str__(self):
        return self.body[0:50]

