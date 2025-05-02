from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    diet = models.CharField(max_length=100, blank=True, null=True)
    allergies = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    max_calories = models.IntegerField(default=0)
    max_carbs = models.IntegerField(default=0)
    max_protein = models.IntegerField(default=0)
    max_fat = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"