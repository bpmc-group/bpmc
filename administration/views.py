from django.shortcuts import render

# def landing_page(request):
#     return render(request, 'administration/landing_page.html')

def application_setup(request):
    return render(request, 'administration/application_setup.html')

def data_import_tool(request):
    return render(request, 'administration/data_import_tool.html')

def setup_data_manager(request):
    return render(request, 'administration/setup_data_manager.html')

def devices(request):
    return render(request, 'administration/devices.html')

def business_processes(request):
    return render(request, 'administration/business_processes.html')

def developer_portal(request):
    return render(request, 'administration/developer_portal.html')
