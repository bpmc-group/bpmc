from django.urls import path
# from .views import landing_page
from . import views

urlpatterns = [
    # path('', landing_page, name='scheduling_landing_page'),
    path('schedule_planner/', views.schedule_planner, name='schedule_planner'),
    path('schedule_planner_transfers/', views.schedule_planner_transfers, name='schedule_planner_transfers'),
    path('time_off_calendar/', views.time_off_calendar, name='time_off_calendar'),
    path('staffing_dashboard/', views.staffing_dashboard, name='staffing_dashboard'),
]
