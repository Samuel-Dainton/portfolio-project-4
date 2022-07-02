from django.contrib import admin
from .models import Recipe, Topic, Comment, Allergy, UserProfile

admin.site.register(Recipe)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Allergy)
admin.site.register(UserProfile)


