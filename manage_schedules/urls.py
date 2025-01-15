from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_home, name='manage_schedules_home'),
]
