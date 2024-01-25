from django.urls import path

from . import views


urlpatterns = [
    path('IndexAppointment/', views. IndexAppointment.as_view(), name='IndexAppointment'),
    path('create/', views.AppointmentCreateView.as_view(), name='create_appointment'),
    path('update/<int:pk>', views.AppointmentUpdateView.as_view(), name='update_appointment'),
    path('read/<int:pk>', views.AppointmentReadView.as_view(), name='read_appointment'),
    path('delete/<int:pk>', views. AppointmentDeleteView.as_view(), name='delete_appointment'),
    path('appointment/', views.appointments, name='appointment'),
    path('ajax/load-dentists/', views.load_dentists, name='ajax_load_dentists'),
    path("searchappointment/",views.SearchAppointmentResultsView.as_view(), name="searchappointment_results"),
    path('generar-pdf/', views.generar_pdf, name='generar_pdf'),
    
]