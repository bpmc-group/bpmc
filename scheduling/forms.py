# scheduling/forms.py
from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['employee', 'date', 'shift_start', 'shift_end']
