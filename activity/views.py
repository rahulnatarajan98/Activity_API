from django.shortcuts import render
from django.http import JsonResponse
from api.models import Member, Activity
from timezone_utils.choices import ALL_TIMEZONES_CHOICES
import datetime

def index(request):
    members = Member.objects.all()
    zones = ALL_TIMEZONES_CHOICES
    return render(request,'index.html', {'zones': zones, 'members': members})