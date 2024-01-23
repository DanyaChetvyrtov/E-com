from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='profile_images')
    contact_numer = models.CharField(max_length=20, default='+7(988)-***-**-**')

    def __str__(self):
        return self.user.username