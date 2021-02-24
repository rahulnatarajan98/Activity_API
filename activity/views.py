from django.shortcuts import render
from django.http import JsonResponse
from api.models import Member, Activity
from timezone_utils.choices import ALL_TIMEZONES_CHOICES
import datetime

def index(request):
    members = Member.objects.all()
    zones = ALL_TIMEZONES_CHOICES
    return render(request,'index.html', {'zones': zones, 'members': members})

def add_member(request):
    if request.method =="GET" and request.is_ajax():
        input_id = request.GET.get('id')
        name = request.GET.get('name')
        tz = request.GET.get('tz')
        if (input_id!="" and name!="" and tz!=""):
            try:
                memObj = Member(id=input_id,real_name=name,tz=tz)
                memObj.save()
                message = "Success"
            except Exception as e:
                message = str(e)
                print(message)
            context = {'message': message}
        else:
            context = {'message': 'One of the Input feild is Empty'}
        return JsonResponse(context,safe=False)

def add_activity(request):
    if request.method =="GET" and request.is_ajax():
        mem = request.GET.get('memb_fk').split('-')
        start_time = request.GET.get('start_time').split('T')
        end_time = request.GET.get('end_time').split('T')
        if mem!="" and start_time!="" and end_time!="":
            memb_obj = Member.objects.get(id=mem[0])

            start_time_str = start_time[0] + " " + start_time[1]
            start_date_time_obj = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')  

            end_time_str = end_time[0] + " " + end_time[1]
            end_date_time_obj = datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')
            
            try:
                actObj = Activity(member=memb_obj,start_time=start_date_time_obj,end_time=end_date_time_obj)
                actObj.save()
                message = "Success"
            except Exception as e:
                message = str(e)
                print(e)
            context = {'message': message}
        else:
            context = {'message': 'One of the Input feild is Empty'}
        return JsonResponse(context,safe=False)