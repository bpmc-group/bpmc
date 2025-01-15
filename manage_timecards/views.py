from django.shortcuts import render

def home(request):
    return render(request, 'manage_timecards/home.html')

