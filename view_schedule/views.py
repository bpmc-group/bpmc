from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Schedule
from api.serializer import ScheduleSerializer

@login_required
def view_schedule(request):
    return render(request, 'view_schedule/schedule.html')

@api_view(['GET'])
def get_schedule(request):
    user = request.user
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    schedules = Schedule.objects.filter(user=user, status="POSTED")
    if start_date:
        schedules = schedules.filter(date__gte=start_date)
    if end_date:
        schedules = schedules.filter(date__lte=end_date)

    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)
