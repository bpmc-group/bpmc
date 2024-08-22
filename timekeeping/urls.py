from django.urls import path
# from .views import landing_page
from . import views

urlpatterns = [
    # path('', landing_page, name='timekeeping_landing_page'),
    path('employee_summary/', views.employee_summary, name='employee_summary'),
    path('timecards/', views.timecards, name='timecards'),
    path('attendance/', views.attendance, name='attendance'),
    path('leave_of_absence/', views.leave_of_absence, name='leave_of_absence'),
    path('overtime_approvals/', views.overtime_approvals, name='overtime_approvals'),
    path('hours_allocation/', views.hours_allocation, name='hours_allocation'),
]
