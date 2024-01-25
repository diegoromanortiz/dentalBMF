from django.db import models
from django.contrib.auth.models import User
from Clinic.models import Clinic
from django.core.validators import MinLengthValidator

class Dentist(models.Model):

    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_card = models.CharField(max_length=11, validators=[
                               MinLengthValidator(11)])
    phone_no = models.CharField(max_length=10, validators=[
                                MinLengthValidator(10)])
    email = models.CharField(max_length=75)
    birth_date = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


