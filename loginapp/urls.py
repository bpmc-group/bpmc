from django.urls import path
from .views import login, dashboard

urlpatterns = [
    path('', login, name='login'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]