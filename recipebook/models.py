from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Avg


# Status for wether recipe is published
STATUS = ((0, "Draft"), (1, "Published"))


# Season Model - category
class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Diet Model - category
class Diet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Recipe Model - deals with all of the recipe metadata
class Recipe(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter()

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
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    objects = models.Manager()
    newmanager = NewManager()

    class Meta:
        ordering = ["-created_on"]

    def average_rating(self) -> float:
        return Rating.objects.filter(
            recipe=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.title}: {self.average_rating()}"


# Rating Model - the user input and passes into recipe to create the avg
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.recipe.title}: {self.rating}"


# Comment Model - Inspired by CodeInstitue
class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
