from rest_framework import serializers
from .models import User, Punch, Schedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punch
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
