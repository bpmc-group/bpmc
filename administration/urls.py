from django.urls import path
# from .views import landing_page
from . import views

urlpatterns = [
    # path('', landing_page, name='administration_landing_page'),
    path('application_setup/', views.application_setup, name='application_setup'),
    path('data_import_tool/', views.data_import_tool, name='data_import_tool'),
    path('setup_data_manager/', views.setup_data_manager, name='setup_data_manager'),
    path('devices/', views.devices, name='devices'),
    path('business_processes/', views.business_processes, name='business_processes'),
    path('developer_portal/', views.developer_portal, name='developer_portal'),
]
