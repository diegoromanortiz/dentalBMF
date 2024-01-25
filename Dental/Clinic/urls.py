from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexClinic.as_view(), name='indexClinic'),
    
    path('create/', views.ClinicCreateView.as_view(), name='create_clinic'),
    path('update/<int:pk>', views.ClinicUpdateView.as_view(), name='update_clinic'),
    path('read/<int:pk>', views.ClinicReadView.as_view(), name='read_clinic'),
    path('delete/<int:pk>', views.ClinicDeleteView.as_view(), name='delete_clinic'),
    path('clinic/', views.clinic, name='clinic'),
   
]