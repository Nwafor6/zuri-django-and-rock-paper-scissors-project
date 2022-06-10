from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def getprofile(request):
    profiles= Profile.objects.all()
    return JsonResponse({"profiles": list(profiles.values())})  