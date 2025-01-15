from django.urls import path
from .views import reporting_landing, export_users_csv


urlpatterns = [
    path('', reporting_landing, name='reporting_landing'),
    path('users/export-csv/', export_users_csv, name='export_users_csv'),
]
