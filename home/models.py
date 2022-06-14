from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    """ Recipe data """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateField(auto_now_add=True)
    intro = models.TextField()
    servings = models.CharField(max_length=2)
    topic = models.ManyToManyField(Topic, blank=False)
    method = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    #likes = models.ManyToManyField(
    #    User, related_name='recipe_like', blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title

    #def number_of_likes(self):
    #    return self.likes.count()

class Ingredients(models.Model):
    """ Ingredients data """
    ingredient = models.CharField(max_length=50) #name of the ingredient
    quantity = models.CharField(max_length=10) #number of the ingredients
    unit = models.CharField(max_length=10) #measurement of the ingredient - lb, kg, ml, teaspoon...


    def __str__(self):
        return self.ingredient

class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name="comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"