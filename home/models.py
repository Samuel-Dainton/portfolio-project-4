from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

from django.db.models.signals import post_save
from django.dispatch import receiver




class UserProfile(models.Model):
    avatar = CloudinaryField('image', blank=True, null=True, default="v1656845904/chef_dvaqcl.png")
    bio = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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
    calories = models.CharField(blank=True, null=True, max_length=50)
    fat = models.CharField(blank=True, null=True, max_length=50)
    carbs = models.CharField(blank=True, null=True, max_length=50)
    protein = models.CharField(blank=True, null=True, max_length=50)

    # housekeeping
    created = models.DateTimeField(auto_now_add=True)
    # thirdparty
    introduction = RichTextField(blank=True, null=True)
    ingredient = RichTextField(blank=False, null=True)
    method = RichTextField(blank=False, null=True)
    image = CloudinaryField('image', null=True, blank=True, default='placeholder')    
    
    @property
    def time(self):
        hours = (self.prep_time + self.cook_time) // 60
        minutes = (self.prep_time + self.cook_time) % 60
        time = "{}h {}min".format(hours, minutes)
        return time
    
    @property
    def hours_prep_time(self):
        hours = self.prep_time // 60
        minutes = self.prep_time % 60
        hours_prep_time = "{}h {}min".format(hours, minutes)
        return hours_prep_time
    
    @property
    def hours_cook_time(self):
        hours = self.cook_time // 60
        minutes = self.cook_time % 60
        hours_cook_time = "{}h {}min".format(hours, minutes)
        return hours_cook_time

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.recipe)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.body[0:50]


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()