from django.db import models
from django.contrib.auth.models import AbstractUser


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()
    image = models.ImageField(upload_to="photos", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username
