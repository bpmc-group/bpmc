from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('home/', views.admin_home, name='admin_home'),
    path('users/', views.user_management, name='user_management'),
    path('add_user/', views.add_user, name='add_user'),
    path('function_access_profiles/', views.function_access_profiles, name='function_access_profiles'),
    path('function_access_profiles/create/', views.create_access_profile, name='create_access_profile'),
    path('function_access_profiles/edit/', views.edit_access_profile, name='edit_access_profile'),
    path('assign_profiles_to_user/', views.assign_profile_to_user, name='assign_profiles_to_user'),
    path('permission_denied/', views.permission_denied, name='permission_denied'),
]

