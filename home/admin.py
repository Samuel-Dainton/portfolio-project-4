from django.contrib import admin
from .models import Recipe, Comment, Topic, Ingredients
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Topic)
admin.site.register(Ingredients)

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on')
    search_fields = ('title', 'method')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('method',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'body', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('email', 'body')