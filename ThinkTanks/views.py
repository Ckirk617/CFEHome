from django.shortcuts import render
from django.http import HttpResponse
from .models import State, City, Organization, PolicyArea, Staff
from rest_framework import viewsets
from .serializers import StateSerializer
from rest_framework.authentication import BasicAuthentication


# Create your views here.
def index(request):
    return render(request, 'ttdirectory/index.html')

def detail(request, title):
    return HttpResponse("You're looking at question %s." % title)

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all().order_by('name')
    serializer_class = StateSerializer
    authentication_classes = (BasicAuthentication,)