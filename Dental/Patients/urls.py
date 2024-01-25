from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'), 
    path('create/', views.PatientCreateView.as_view(), name='create_patient'),
    path('update/<int:pk>', views.PatientUpdateView.as_view(), name='update_patient'),
    path('read/<int:pk>', views.PatientReadView.as_view(), name='read_patient'),
    path('delete/<int:pk>', views.PatientDeleteView.as_view(), name='delete_patient'),
    path('patient/', views.patients, name='patient'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("search/",views.SearchResultsView.as_view(), name="search_results"),
   
    
    ]