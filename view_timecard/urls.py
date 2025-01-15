from django.urls import path
from .views import view_timecard, get_timecard

urlpatterns = [
    path('', view_timecard, name='view_timecard'),
    path('data/', get_timecard, name='get_timecard'),
]
