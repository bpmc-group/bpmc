from django.shortcuts import render

# def landing_page(request): I'm testing the push update git. 
#     return render(request, 'timekeeping/landing_page.html')

def employee_summary(request):
    return render(request, 'timekeeping/employee_summary.html')

def timecards(request):
    return render(request, 'timekeeping/timecards.html')

def attendance(request):
    return render(request, 'timekeeping/attendance.html')

def leave_of_absence(request):
    return render(request, 'timekeeping/leave_of_absence.html')

def overtime_approvals(request):
    return render(request, 'timekeeping/overtime_approvals.html')

def hours_allocation(request):
    return render(request, 'timekeeping/hours_allocation.html')

