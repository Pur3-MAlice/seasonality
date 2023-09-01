from django.contrib import admin
from .models import Recipe, Diet, Comment
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Diet)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'diet')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content', 'ingredients')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'approved', 'created_on', 'recipe')
    search_fields = ['name', 'body']
    actions = ['close_comments']

    def close_comments(Self, request, queryset):
        queryset.update(approved=False)
