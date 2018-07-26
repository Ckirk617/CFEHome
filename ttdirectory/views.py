from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'ttdirectory/index.html')

def detail(request, title):
    return HttpResponse("You're looking at question %s." % title)
