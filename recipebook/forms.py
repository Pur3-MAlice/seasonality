from .models import Comment, Recipe
from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author', 'favourites',)
        fields = (
            'title',
            'slug',
            'author',
            'diet',
            'season',
            'featured_image',
            'status',
            'content',
            'ingredients',
            'calories',
            'fat',
            'protein',
            'carbs',
            'servs',
            'favourites',
        )
        widgets = {
            'content': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'slug': forms.TextInput(attrs={'type': 'hidden'}),
            'status': forms.TextInput(attrs={'type': 'hidden'})
        }
        prepopulated_fields = {'slug': ('title',)}
