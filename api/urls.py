from django.urls import path
from . import views
from .views import get_users, create_user, user_detail, get_punches, create_punch, punch_detail, get_schedules, create_schedule, update_schedules, delete_schedule

urlpatterns = [
    # Users
    path('users/', get_users, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail'),


    # Punches
    path('punches/', get_punches, name='get_punches'),
    path('punches/create/', create_punch, name='create_punch'),
    path('punches/<int:pk>/', punch_detail, name='punch_detail'),

    # Schedules
    path('schedules/', get_schedules, name='get_schedules'),
    path('schedules/create/', create_schedule, name='create_schedule'),
    path('schedules/<int:pk>/', update_schedules, name='update_schedule'),
    path('schedules/<int:pk>/delete/', delete_schedule, name='delete_schedule'),
]