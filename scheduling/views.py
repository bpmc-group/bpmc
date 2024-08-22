from django.shortcuts import render
from .models import Schedule
from datetime import datetime, timedelta

# scheduling/views.py
from django.shortcuts import render
from .models import Schedule, Employee
from datetime import datetime, timedelta

# scheduling/views.py
from django.shortcuts import render
from django.utils.dateparse import parse_date
from datetime import date, timedelta

def schedule_planner(request):
    # Sample data for dates
    dates = [date.today() + timedelta(days=i) for i in range(7)]

    context = {
        'dates': dates,
    }
    return render(request, 'scheduling/schedule_planner.html', context)


def schedule_planner_transfers(request):
    return render(request, 'scheduling/schedule_planner_transfers.html')
    
def time_off_calendar(request):
    return render(request, 'scheduling/time_off_calendar.html')
    
def staffing_dashboard(request):
    return render(request, 'scheduling/staffing_dashboard.html')
