from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from places.fields import PlacesField


class User(AbstractUser):
    username = None
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    birthdate = models.DateField()
    address = PlacesField(null=True, blank=True)
    phone_no = models.CharField(max_length=8)
    avatar = models.ImageField(blank=True,null=True, upload_to="avatars/")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def __str__(self):
        return "{}".format(self.username)


class UserBio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=False)

    def __str__(self):
        return f'{self.bio}'
