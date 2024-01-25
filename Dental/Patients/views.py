from typing import Any, Dict
from django import forms
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic


from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
  
    PatientsModelForm,
    CustomAuthenticationForm,
    CustomUserCreationForm
)
from .models import Patients
from django.db.models import Q 
from django.views.generic import ListView
from django.db.models import Q
from .widgets import DateInput
from .models import Patients





class Index(generic.ListView):
    model = Patients
    context_object_name = 'patients'
    template_name = 'index.html'
    paginate_by = 10
    queryset = Patients.objects.all().order_by('last_name')
    
class SearchResultsView(ListView):
    context_object_name = 'patients'
    model = Patients
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get("q") # new
        return Patients.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)|
            Q(phone_no__icontains=query)
        )
        
    
class PatientCreateView(BSModalCreateView):
    template_name = 'examples/create_patient.html'
    form_class =  PatientsModelForm
    success_message = 'Success:Patient Created.'
    success_url = reverse_lazy('IndexAppointment')

    def get_form(self, form_class=None):
        form = super(PatientCreateView, self).get_form(form_class)
        form.fields['birth_date'].widget = DateInput()  # Asigna el widget personalizado
        return form

class PatientUpdateView(BSModalUpdateView):
    model = Patients
    template_name = 'examples/update_patient.html'
    form_class =  PatientsModelForm
    success_url = reverse_lazy('index')
    success_message = 'Success: updated patient.'
   

class PatientReadView(BSModalReadView):
    model = Patients
    template_name = 'examples/read_patient.html'
    

class PatientDeleteView(BSModalDeleteView):
    model = Patients
    template_name = 'examples/delete_patient.html'
    success_message = 'Success: Eliminated patient.'
    success_url = reverse_lazy('index')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'examples/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'examples/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')


def patients(request):
    data = dict()
    if request.method == 'GET':
        patients = Patients.objects.all()
        data['table'] = render_to_string(
            '_patients_table.html',
            {'patients': patients},
            request=request
        )
        return JsonResponse(data)
    



