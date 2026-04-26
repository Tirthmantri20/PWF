from django.urls import path
from .views import CompanyListCreateView, CompanyRetrieveUpdateView
from . import views

urlpatterns = [
    path('api/companies/', CompanyListCreateView.as_view(), name='company_list_create'),
    path('api/companies/<int:pk>/', CompanyRetrieveUpdateView.as_view(), name='company_detail'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/new/', views.job_create, name='job_create'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
]