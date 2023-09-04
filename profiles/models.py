from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
