from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on')
    search_fields = ('title', 'method')
    prepopulated_fields = {'slug': ('title',)}
    list_filer = ('status', 'created_on')
    summernote_fields = ('method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filer = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['delete_comments']

    def delete_comments(self, request, queryset):
        queryset.update(approved=False)
# Register your models here.
