from django.shortcuts import render

def schedule_home(request):
    return render(request, 'manage_schedules/home.html', {'title': 'Manage Schedules'})
