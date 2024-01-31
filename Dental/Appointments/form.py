from django.contrib.auth.models import User
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Appointment
from Patients.models import Patients
from .widgets import DateTimePickerInput
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
class DateInput(forms.DateInput):
  
    input_type = 'date'



class AppointmentModelForm(BSModalModelForm):
   
   
    class Meta:

        model =  Appointment
        fields =['appointment_reason','clinic','patient','dentist','date']
        

        widgets = {
            "date":DateTimePickerInput(options={"format": "DD/MM/YYYY HH:mm ",
                                                "daysOfWeekDisabled":[0,6],
                                                "stepping": [30,00],
                                                "enabledHours": [ 8,9,10,11,12,15,16,17,18,19,20 ]},
                                       )
            
            }
                                     

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtener el último paciente registrado
        last_patient = Patients.objects.last()
        
        if last_patient:
            # Establecer el valor predeterminado del campo 'patient'
            self.fields['patient'].initial = last_patient.pk
           
        

        



