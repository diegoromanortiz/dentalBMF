from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Dentist
from django_flatpickr.schemas import FlatpickrOptions
from .widgets import DateInput




class DentistsModelForm(BSModalModelForm):
    
    first_name = forms.CharField(min_length=3,max_length=50)
    last_name = forms.CharField(min_length=3,max_length=50)
   
    class Meta:

        model = Dentist
        fields ='__all__'

        widgets = {
          "email":forms.EmailInput(), 
          "phone_no":forms.NumberInput(),
          "birth_date":DateInput(),
             
          
        }

