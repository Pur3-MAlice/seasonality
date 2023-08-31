from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    repopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content', 'ingredients')
