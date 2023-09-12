from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):  # Admin page, adds profile elements
    list_display = ('user', 'bio')
    list_filter = ('user', )
    search_fields = ['user', 'bio']
    summernote_fields = ('user', 'bio')
