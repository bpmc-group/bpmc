# scheduling/models.py
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Schedule(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    shift_start = models.TimeField()
    shift_end = models.TimeField()

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.shift_start} to {self.shift_end}"
