from django.urls import path
from api.models import Punch
from . import views

urlpatterns = [
    path('', views.punch_landing, name='punch_landing'),  # Landing page for punches
]
