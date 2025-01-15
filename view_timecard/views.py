from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Punch
from api.serializer import PunchSerializer

@login_required
def view_timecard(request):
    return render(request, 'view_timecard/timecard.html')

@api_view(['GET'])
def get_timecard(request):
    user = request.user
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    punches = Punch.objects.filter(user=user)
    if start_date:
        punches = punches.filter(punch_time__gte=start_date)
    if end_date:
        punches = punches.filter(punch_time__lte=end_date)

    serializer = PunchSerializer(punches, many=True)
    return Response(serializer.data)
