from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Punch, Schedule
from .serializer import UserSerializer, PunchSerializer, ScheduleSerializer
import logging
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import AccessProfile, Permission
from django.shortcuts import get_object_or_404


# Setup logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    data = request.data
    if 'password' in data:
        data['password'] = make_password(data['password'])  # Hash the password

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        logger.info(f"Received {request.method} request for user ID: {pk}")
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        logger.warning(f"User with ID {pk} not found.")
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        logger.info(f"GET response for user ID {pk}: {serializer.data}")
        return Response(serializer.data)

    elif request.method == 'PUT':
        logger.info(f"PUT request data for user ID {pk}: {request.data}")
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"User ID {pk} updated successfully: {serializer.data}")
            return Response(serializer.data)
        logger.error(f"Validation errors for user ID {pk}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        logger.info(f"User ID {pk} deleted successfully.")
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def get_punches(request):
#     punches = Punch.objects.all()
#     serializer = PunchSerializer(punches, many=True)
#     logger.info("Fetched all punches.")
#     return Response(serializer.data)

@api_view(['GET'])
def get_punches(request):
    user_id = request.query_params.get('user')
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    # Validate user parameter
    if not user_id:
        return Response({'error': 'User ID is required.'}, status=400)

    user = get_object_or_404(User, id=user_id)
    punches = Punch.objects.filter(user=user)

    # Apply date filters
    if start_date:
        punches = punches.filter(punch_time__gte=start_date)
    if end_date:
        punches = punches.filter(punch_time__lte=end_date)

    serializer = PunchSerializer(punches, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_punch(request):
    print("Function create_punch was called") 
    data = request.data
    print("Received Data:", data)

    # Validate and fetch the user object
    try:
        user = User.objects.get(pk=data.get('user_id'))
        data['user'] = user.id  # Assign the user ID to the `user` field
    except User.DoesNotExist:
        return Response({'success': False, 'error': 'Invalid user ID provided.'}, status=status.HTTP_400_BAD_REQUEST)

    # Set default punch_time if not provided
    data['punch_time'] = data.get('punch_time', now().isoformat())
    print("Processed Data with Default Time:", data)

    serializer = PunchSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        print("Punch Created:", serializer.data)  # Log successful data
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)

    # Log validation errors
    print("Serializer Errors:", serializer.errors)
    return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def punch_detail(request, pk):
    try:
        punch = Punch.objects.get(pk=pk)
        logger.info(f"Punch with ID {pk} found.")
    except Punch.DoesNotExist:
        logger.warning(f"Punch with ID {pk} not found.")
        return Response({'error': 'Punch not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PunchSerializer(punch)
        logger.info(f"GET response for punch ID {pk}: {serializer.data}")
        return Response(serializer.data)

    elif request.method == 'PUT':
        logger.info(f"PUT request data for punch ID {pk}: {request.data}")
        serializer = PunchSerializer(punch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Punch ID {pk} updated successfully: {serializer.data}")
            return Response(serializer.data)
        logger.error(f"Validation errors for punch ID {pk}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        punch.delete()
        logger.info(f"Punch ID {pk} deleted successfully.")
        return Response({'message': 'Punch deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def permission_required(view_func, function_name, action):
        def wrapped_view(request, *args, **kwargs):
            user_profiles = request.user.access_profiles.all()
            permissions = Permission.objects.filter(
                access_profile__in=user_profiles,
                function_name=function_name,
                **{f"can_{action}": True},
            )
            if permissions.exists():
                return view_func(request, *args, **kwargs)
            return redirect("permission_denied")  # Redirect to a permission denied page

        return wrapped_view

@api_view(['GET'])
def get_schedules(request):
    try:
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        schedules = Schedule.objects.all()
        if user_id:
            schedules = schedules.filter(user_id=user_id)
        if start_date:
            schedules = schedules.filter(date__gte=start_date)
        if end_date:
            schedules = schedules.filter(date__lte=end_date)

        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Error fetching schedules: {str(e)}")
        return Response({"error": "An error occurred while fetching schedules"}, status=500)

@api_view(['POST'])
def create_schedule(request):
    try:
        data = request.data
        logger.info(f"Received data: {data}")  # Log incoming data for debugging

        # Handle batch creation
        serializer = ScheduleSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Schedules saved successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.error(f"Validation errors: {serializer.errors}")  # Log validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        logger.exception(f"Error in create_schedule: {str(e)}")  # Log the exception
        return Response({"error": "An error occurred while saving schedules."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_schedules(request):
    try:
        schedules = request.data  # Expecting a list of schedules
        for schedule in schedules:
            schedule_instance = Schedule.objects.get(pk=schedule['id'])
            schedule_instance.status = schedule['status']
            schedule_instance.save()

        return Response({"message": "Schedules updated successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_schedule(request, pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
        schedule.delete()
        return Response({'message': 'Schedule deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Schedule.DoesNotExist:
        return Response({'error': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)
