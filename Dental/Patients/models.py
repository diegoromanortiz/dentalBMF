from django.db import models
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models import Q 
class Patients(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_card = models.CharField(max_length=11, null=True, validators=[
                               MinLengthValidator(11)])
    phone_no = models.CharField(max_length=10, validators=[
                                MinLengthValidator(10)])
    email = models.CharField(max_length=75)
    birth_date = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True, blank=True)
    

    status = models.CharField(max_length=20, choices=STATUS, default='Active')
   
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
