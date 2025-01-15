from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now
from api.models import User, Punch
from administration.views import permission_required

@permission_required("Punch Management")  # Pass the required `function_name` argument
def punch_landing(request):
    return render(request, 'punch/punch_landing.html')
