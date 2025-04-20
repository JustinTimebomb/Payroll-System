from django.urls import path
from . import views

urlpatterns = [
    path('payroll-report/', views.payroll_report, name='payroll_report'),
    path('payroll-report/print/<int:pk>/', views.print_payroll, name='print_payroll'),  # New URL
]