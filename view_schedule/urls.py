from django.urls import path
from .views import view_schedule, get_schedule

urlpatterns = [
    path('', view_schedule, name='view_schedule'),
    path('data/', get_schedule, name='get_schedule'),
]
