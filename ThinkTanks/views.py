from django.shortcuts import render
from django.http import HttpResponse
from .models import State, City, Organization, PolicyArea, Staff
from rest_framework import viewsets
from .serializers import StateSerializer, CitySerializer, PolicyAreaSerializer, StaffSerializer, OrganizationSerializer
from rest_framework.authentication import BasicAuthentication


# Create your views here.
def index(request):
    return render(request, 'ThinkTanks/index.html')

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all().order_by('name')
    serializer_class = StateSerializer
    authentication_classes = (BasicAuthentication,)
    
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer
    authentication_classes = (BasicAuthentication,)
    
class PolicyAreaViewSet(viewsets.ModelViewSet):
    queryset = PolicyArea.objects.all().order_by('topic')
    serializer_class = PolicyAreaSerializer
    authentication_classes = (BasicAuthentication,)
    
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('name')
    serializer_class = StaffSerializer
    authentication_classes = (BasicAuthentication,)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('name')
    serializer_class = OrganizationSerializer
    authentication_classes = (BasicAuthentication,)