from typing import Any
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.shortcuts import render
from django_flatpickr.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    TimePickerInput,
)
from datetime import datetime
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView,
    BSModalFormView
)
from django.views.generic import View
from .form import (

    AppointmentModelForm
)
from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from .models import Appointment
from Dentists.models import Dentist

from datetime import datetime, timedelta
from django.utils import timezone
from django.urls import reverse_lazy,reverse
from django.utils import timezone


this_week = timezone.now() - timedelta(days=1)


class IndexAppointment(generic.ListView):
    model = Appointment
    #queryset = Appointment.objects.order_by('-clinic')
    queryset = Appointment.objects.filter(date__gte=this_week, date__week_day__range=(
        2, 6), date__hour__range=(8, 20)).order_by('date')
    context_object_name = 'appointments'
    template_name = 'indexAppointment.html'
    paginate_by = 10 


class SearchAppointmentResultsView(ListView):
    context_object_name = 'appointments'
    model = Appointment
    template_name = 'indexAppointment.html'
    success_url = reverse_lazy('IndexAppointment')

    def get_queryset(self):
        query = self.request.GET.get("q")  # new
        return Appointment.objects.filter(date__gte=this_week, date__week_day__range=(2, 6), date__hour__range=(8, 20)).order_by('date').filter(
            Q(date__date__icontains=query) |
            Q(clinic__name__icontains=query) |
            Q(dentist__first_name__icontains=query) |
            Q(dentist__last_name__icontains=query) |
            Q(patient__first_name__icontains=query) |
            Q(patient__last_name__icontains=query)
        )


class AppointmentCreateView(BSModalCreateView):

    template_name = 'examples/create.html'
    form_class = AppointmentModelForm
    success_message = 'Success:Appointment Created.'
    success_url = reverse_lazy('index')

   

class AppointmentUpdateView(BSModalUpdateView):
    model = Appointment
    template_name = 'examples/update.html'
    form_class = AppointmentModelForm
    success_message = 'Success:Appointment updated.'
    success_url = reverse_lazy('IndexAppointment')

class AppointmentReadView(BSModalReadView):
    model = Appointment
    template_name = 'examples/read.html'


class AppointmentDeleteView(BSModalDeleteView):
    model = Appointment
    template_name = 'examples/delete.html'
    success_message = 'Success: Eliminated appointment.'
    success_url = reverse_lazy('IndexAppointment')

# class AppointmentTurnsGivenView(BSModalReadView):
    #model = Appointment
    #template_name = 'example/turnsGiven.html'


def appointments(request):
    data = dict()
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        data['table'] = render_to_string(
            '_appointments_table.html',
            {'appointments': appointments},
            request=request
        )
        return JsonResponse(data)


def load_dentists(request):
    clinic_id = request.GET.get('clinic')
    dentists = Dentist.objects.filter(
        clinic_id=clinic_id).order_by('first_name')
    return render(request, 'hr/dentist_dropdown_list_options.html', {'dentists': dentists})




def obtener_datos_cita():
  
    cita = Appointment.objects.filter().last()
    cita.date = cita.date - timedelta(hours=3)
    datos_cita = {
        'appointment_reason': cita.appointment_reason,
        'clinic': cita.clinic,
        'patient': cita.patient,
        'dentist': cita.dentist,
        'date':cita.date.strftime("%d-%b-%Y-%H:%M"),
       
        # Agrega otros campos de la cita que desees incluir en el PDF
    }

    return datos_cita

def generar_pdf(request):
    # Obtener los datos de la cita recién sacada
    datos_cita = obtener_datos_cita() # Debes implementar esta función para obtener los datos

    # Crear el objeto HttpResponse con el tipo de contenido "application/pdf"
    response = HttpResponse(content_type='application/pdf')
    # Especificar el nombre del archivo PDF que se descargará
    response['Content-Disposition'] = 'attachment; filename="Appointment.pdf"'

    # Crear el objeto Canvas para generar el PDF en la respuesta
    p = canvas.Canvas(response, pagesize=letter)
# Separar la fecha y la hora de la cadena obtenida
   
    # Aquí puedes agregar los datos de la cita recién sacada al PDF
    p.drawString(100, 700, "appointment_reason: {}".format(datos_cita['appointment_reason']))
    p.drawString(100, 680, "clinic: {}".format(datos_cita['clinic']))
    p.drawString(100, 660, "patient: {}".format(datos_cita['patient']))
    p.drawString(100, 640, "dentist: {}".format(datos_cita['dentist']))
    p.drawString(100, 620, "date: {}".format(datos_cita['date']))
    
    # Agrega más datos de la cita según sea necesario...

    # Finaliza la creación del PDF
    p.save()

    return response
