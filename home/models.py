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

class Recipe(models.Model):
    # relationships
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ManyToManyField(Topic,)
    title = models.CharField(max_length=200)
    # basics
    prep_time = models.CharField(null=True, blank=True, max_length=50)
    cook_time = models.CharField(null=True, blank=True, max_length=50)
    difficulty = models.CharField(max_length=50)
    servings = models.CharField(max_length=50)
    calories = models.CharField(blank=True, null=True, max_length=50)
    fat = models.CharField(blank=True, null=True, max_length=50)
    carbs = models.CharField(blank=True, null=True, max_length=50)
    protein = models.CharField(blank=True, null=True, max_length=50)
    allergy_info = models.TextField(blank=True, null=True)
    # housekeeping
    created = models.DateTimeField(auto_now_add=True)
    # thirdparty
    introduction = RichTextField(blank=True, null=True)
    method = RichTextField(blank=True, null=True)
    image = CloudinaryField('image', null=True, blank=True, default="recipe_image.png")    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=50)
    # TODO should it not be positive int field?
    quantity = models.CharField(max_length=10)
    unit = models.CharField(max_length=50, blank=True, null=True)

    description = models.CharField(max_length=50, blank=True, null=True) # Stems seperated, crushed, peeled
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    # TODO reset database change ingredients to singular
    class Meta:
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.ingredient

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.body[0:50]

