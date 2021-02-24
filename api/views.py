from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets
from .models import Member, Activity
from .serializers import MainSerializer

class MemberViewset(viewsets.ModelViewSet):
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