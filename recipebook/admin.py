from django.contrib import admin
from .models import Recipe, Diet
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Diet)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    repopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'diet')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content', 'ingredients')
