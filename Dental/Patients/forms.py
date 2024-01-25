from bootstrap_modal_forms.forms import BSModalForm, BSModalModelForm
from bootstrap_modal_forms.mixins import CreateUpdateAjaxMixin, PopRequestMixin
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Patients
from .widgets import DateInput



class PatientsModelForm(BSModalModelForm):
  
    first_name = forms.CharField(min_length=3,max_length=50)
    last_name = forms.CharField(min_length=3,max_length=50)
    
    class Meta:

        model = Patients
        fields ='__all__'

        widgets = {
          "email":forms.EmailInput(), 
          "phone_no":forms.NumberInput(),
          "birth_date": DateInput(),
         
        }






class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']