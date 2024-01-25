from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
   ClinicModelForm,
)
from .models import Clinic 


class IndexClinic(generic.ListView):
    model = Clinic
    context_object_name = 'clinics'
    template_name = 'indexClinic.html'
    paginate_by = 5
  
class ClinicCreateView(BSModalCreateView):
    template_name = 'clinic/create.html'
    form_class =  ClinicModelForm
    success_message = 'Success: Created CLINIC.'
    success_url = reverse_lazy('indexClinic')


class ClinicUpdateView(BSModalUpdateView):
    model = Clinic
    template_name = 'clinic/update.html'
    form_class =  ClinicModelForm
    success_message = 'Success: Updated CLINIC.'
    success_url = reverse_lazy('indexClinic')


class ClinicReadView(BSModalReadView):
    model = Clinic
    template_name = 'clinic/read.html'
    

class ClinicDeleteView(BSModalDeleteView):
    model = Clinic
    template_name = 'clinic/delete.html'
    success_message = 'Success: Eliminated CLINIC.'
    success_url = reverse_lazy('indexClinic')

def clinic(request):
    data = dict()
    if request.method == 'GET':
        clinic = Clinic.objects.all()
        data['table'] = render_to_string(
            '_clinic_table.html',
            {'clinic': clinic},
            request=request
        )
        return JsonResponse(data)
