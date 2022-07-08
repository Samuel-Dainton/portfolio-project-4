from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from ckeditor.fields import RichTextField

from cloudinary.models import CloudinaryField


class UserProfile(models.Model):

    # relationships
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # basics
    bio = models.CharField(max_length=400, blank=True, null=True)

    # thirdparty    
    avatar = CloudinaryField('image', blank=True, null=True, default="v1656845904/chef_dvaqcl.png")


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Allergy(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    DIFFICULTY_CHOICES = (
        ('Easy','Easy'),
        ('Moderate', 'Moderate'),
        ('Advanced','Advanced'),
    )

    # relationships
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ManyToManyField(Topic,)
    allergy_info = models.ManyToManyField(Allergy,)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    
    # basics
    title = models.CharField(max_length=200, unique=True)
    prep_time = models.PositiveIntegerField(null=True, blank=False)
    cook_time = models.PositiveIntegerField(null=True, blank=False)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES, default='Easy')
    servings = models.CharField(max_length=50)
    calories = models.PositiveIntegerField(blank=True, null=True)
    fat = models.PositiveIntegerField(blank=True, null=True)
    carbs = models.PositiveIntegerField(blank=True, null=True)
    protein = models.PositiveIntegerField(blank=True, null=True)

    # housekeeping
    created = models.DateTimeField(auto_now_add=True)

    # thirdparty
    introduction = models.TextField(blank=True, null=True, default='ici')
    ingredient = models.TextField(blank=False, null=True, default='ici')
    method = models.TextField(blank=False, null=True, default='ici')
    image = CloudinaryField('image', null=True, blank=True, default='placeholder')    

    """
    Next three functions are to convert minutes from recipe forms into hours and minutes.
    'Time' adds both the prep time and cook time to give a total for the recipe grid.
    """
    @property
    def time(self):
        hours = (self.prep_time + self.cook_time) // 60
        minutes = (self.prep_time + self.cook_time) % 60
        time = "{}hr {}min".format(hours, minutes)
        return time
    
    @property
    def hours_prep_time(self):
        hours = self.prep_time // 60
        minutes = self.prep_time % 60
        hours_prep_time = "{}hr {}min".format(hours, minutes)
        return hours_prep_time
    
    @property
    def hours_cook_time(self):
        hours = self.cook_time // 60
        minutes = self.cook_time % 60
        hours_cook_time = "{}hr {}min".format(hours, minutes)
        return hours_cook_time
   
    @property
    def num_likes(self):
        return self.liked.all().count()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Like(models.Model):

    LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
    )

    # relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    # basics
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.recipe)


class Comment(models.Model):

    # relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    # thirdparty
    body = RichTextField()

    # housekeeping
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body[0:50]


# Extends the user model with a userprofile when a new user is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()