from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import viewsets
from .models import Member, Activity
from .serializers import MainSerializer, MemberSerializer, ActivitySerializer, ActivityPostSerializer

class MemberViewset(viewsets.ModelViewSet):
    '''
        Lists all the members and the activity.
        ok: True - if data exits
        ok: False - if no data exists
    '''
    queryset = Member.objects.all()
    serializer_class = MainSerializer

    def list(self, request, *args, **kwargs):
        queryset = Member.objects.all()
        if queryset:
            api_data = {
                'ok': True,
                'members': MainSerializer(self.get_queryset(),many=True).data
            }
        else:
            api_data = {
                'ok': False,
                'members': "No Data Available"
            }
        return Response(api_data)

@csrf_exempt
def other_member(request):
    '''
        POST & DELETE data to members
    '''
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'Message': "Data added Succesfully"}, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        try:
            data = JSONParser().parse(request)
            member = Member.objects.get(id=data['id'])
            member.delete()
            return JsonResponse({'Message': "Deleted Succesfully"}, status=201)
        except exceptions.ObjectDoesNotExist:
            return JsonResponse({'Message': "Member does not exist"}, status=400)
        except Exception as e:
            return JsonResponse({'Message': str(e)}, status=400)

@csrf_exempt
def other_activity(request):
    '''
        POST & DELETE data to activity.
    '''
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            if data['start_time'] <= data['end_time']:
                serializer = ActivityPostSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'Message': "Data added Succesfully"}, status=201)
                else:
                    return JsonResponse({'Error': serializer.errors}, status=400)
            else:
                return JsonResponse({'Error': "Date issue"}, status=400)
        except Exception as e:
            print (e)
            return JsonResponse({'Error': str(e)}, status=400)
    
    elif request.method == "DELETE":
        try:
            data = JSONParser().parse(request)
            activity = Activity.objects.get(member=data['member'], start_time=data['start_time'], end_time=data['end_time'])
            activity.delete()
            return JsonResponse({'Message': "Deleted Succesfully"}, status=201)
        except exceptions.ObjectDoesNotExist:
            return JsonResponse({'Message': "Activity does not exist"}, status=400)
        except Exception as e:
            return JsonResponse({'Message': str(e)}, status=400)