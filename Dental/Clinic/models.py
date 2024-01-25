from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator


class Clinic(models.Model):
    name = models.CharField(max_length=30)
    rnc = models.CharField(max_length=9)

    def __str__(self) -> str:
        return self.name

