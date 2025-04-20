from django.shortcuts import render, get_object_or_404
from .models import Payroll

def payroll_report(request):
    payrolls = Payroll.objects.all()
    context = {
        'payrolls': payrolls,
        'currency': '₱',  # Example currency symbol
    }
    return render(request, 'reports/payroll_report.html', context)

def print_payroll(request, pk):
    # Fetch the payroll record for the specified employee
    payroll = get_object_or_404(Payroll, id=pk)
    context = {
        'payroll': payroll,
        'currency': '₱',  # Example currency symbol
    }
    return render(request, 'reports/print_payroll.html', context)