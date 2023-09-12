from .models import Comment, Recipe
from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):  # Form for user's comments
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):   # Form for adding and editing recipes
    class Meta:
        model = Recipe
        exclude = ('author', 'favourites', 'featured_image',)
        fields = (
            'title',
            'slug',
            'author',
            'calories',
            'fat',
            'protein',
            'carbs',
            'servs',
            'diet',
            'season',
            'status',
            'ingredients',
            'content',
            'favourites',
        )
        widgets = {
            'content': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'slug': forms.TextInput(attrs={'type': 'hidden'}),
            'status': forms.TextInput(attrs={'type': 'hidden'})
        }
        prepopulated_fields = {'slug': ('title',)}
