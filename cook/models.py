from django.db import models
from django.contrib.auth.models import AbstractUser


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    def __str__(self) -> str:
        return self.username
