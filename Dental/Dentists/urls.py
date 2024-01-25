from django.urls import path

from . import views

()
urlpatterns = [
    path('indexDentists/', views. IndexDentist.as_view(), name='indexDentists'),
    path('create/', views.DentistCreateView.as_view(), name='create_dentist'),
    path('update/<int:pk>', views.DentistUpdateView.as_view(), name='update_dentist'),
    path('read/<int:pk>', views.DentistReadView.as_view(), name='read_dentist'),
    path('delete/<int:pk>', views.DentistDeleteView.as_view(), name='delete_dentist'),
    path('dentist/', views.dentists, name='dentist'),
   
]