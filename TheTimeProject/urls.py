"""
URL configuration for TheTimeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls), #default
    path('api/', include('api.urls')), # api app
    path('auth/', include('authentication.urls')), # authentication/home app
    path('', lambda request: redirect('auth/login/')), # authentication/home app
    path('administration/', include('administration.urls')),  # Administration app
    path('manage_timecards/', include('manage_timecards.urls')), # Manager Timecards app
    path('manage-schedules/', include('manage_schedules.urls')), # Manager Schedules app
    path('manage-schedules/', include('manage_schedules.urls')),
    path('punch/', include('punch.urls')),  # Punch App
    path('view-timecard/', include('view_timecard.urls')),
    path('view-schedule/', include('view_schedule.urls')),
    path('reporting/', include('reporting.urls')),
]
