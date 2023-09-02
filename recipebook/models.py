from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Diet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    diet = models.ForeignKey(
        Diet, on_delete=models.CASCADE, default=True, null=False)
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, default=True, null=False)
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    ingredients = models.TextField(default='placeholder')
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    servs = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
