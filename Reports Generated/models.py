from django.db import models

class Employee(models.Model):
    EMPLOYEE_TYPES = (
        ('regular', 'Regular'),
        ('probationary', 'Probationary'),
        ('contractual', 'Contractual'),
    )
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPES)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calculate net pay
        self.net_pay = self.basic_salary + self.overtime_pay - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payroll for {self.employee} from {self.date_from} to {self.date_to}"