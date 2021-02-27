from rest_framework import serializers
from .models import Member, Activity

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['start_time','end_time']


class ActivityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class MainSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True)

    class Meta:
        model = Member
        fields = ['id','real_name','tz','activity_periods']