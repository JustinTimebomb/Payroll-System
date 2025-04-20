from django.contrib import admin
from .models import Employee, Payroll

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'position', 'employment_type', 'daily_rate')
    search_fields = ('first_name', 'last_name', 'employee_id')

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date_from', 'date_to', 'basic_salary', 'overtime_pay', 'deductions', 'net_pay')
    list_filter = ('date_from', 'date_to')
    search_fields = ('employee__first_name', 'employee__last_name')