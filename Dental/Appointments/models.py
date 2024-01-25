from django.db import models
from Clinic.models import Clinic
from Dentists.models import Dentist
from Patients.models import  Patients

# file: polls/models.py
import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

#def ultimo():
    #ultimo=Patients.objects.filter().last()
    #return ultimo

class Appointment(models.Model):

    REASON = (
        ('GC', 'General Consultation'),
        ('DC', 'Dental cleaning'),
        ('CR', 'Crowns'),
        ('BR', 'Braces'),
        ('TW', 'Teeth whitening'),
    )
 

    appointment_reason = models.CharField(
        max_length=2, choices=REASON, default='CG')
    
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients,on_delete=models.CASCADE,related_query_name="patient")
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    #hour = models.TimeField(['%H:%M'], blank=True, null=True,unique=True)fechaSalida = models.DateField(verbose_name="Fecha de salida",auto_now=False,auto_now_add=True)
    
    def clean(self):
        

        # Verificar que la fecha sea futura.
        if self.date <= timezone.now():
            raise ValidationError('La fecha debe ser en el futuro.')
        
        if Appointment.objects.filter(appointment_reason =self.appointment_reason ,dentist=self.dentist, date=self.date).exists():
            raise ValidationError('El turno solicitado para este dentista ya esta dado')  

        
        



    


    
    
    