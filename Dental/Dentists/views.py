from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView,
   
)

from .form import (
   DateInput, 
  DentistsModelForm,
)
from .models import Dentist
from .form import DateInput


class IndexDentist(generic.ListView):
    model = Dentist
    context_object_name = 'dentists'
    template_name = 'indexDentists.html'
    queryset=Dentist.objects.all().order_by('clinic')


class DentistCreateView(BSModalCreateView):
    template_name = 'dentists/create.html'
    form_class =  DentistsModelForm
    success_message = 'Success:Dentist Created.'
    success_url = reverse_lazy('indexDentists')

    def get_form(self, form_class=None):
        form = super(DentistCreateView, self).get_form(form_class)
        form.fields['birth_date'].widget = DateInput()
        return form

class DentistUpdateView(BSModalUpdateView):
    model = Dentist
    template_name = 'dentists/update.html'
    form_class =  DentistsModelForm
    success_url = reverse_lazy('indexDentists')

    

class DentistReadView(BSModalReadView):
    model = Dentist
    template_name = 'dentists/read.html'
    

class DentistDeleteView(BSModalDeleteView):
    model = Dentist
    template_name = 'dentists/delete.html'
    success_message = 'Success: Eliminated dentist.'
    success_url = reverse_lazy('indexDentists')



def dentists(request):
    data = dict()
    if request.method == 'GET':
        dentists = Dentist.objects.all()
        data['table'] = render_to_string(
            '_dentists_table.html',
            {'dentist': dentists},
            request=request
        )
        return JsonResponse(data)
