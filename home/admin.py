from django.contrib import admin
from .models import Recipe, Topic, Ingredient, Comment

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    list_display = ['title', 'author']
    raw_id_fields = ['author']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Topic)
admin.site.register(Comment)




