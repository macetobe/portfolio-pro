from django.shortcuts import render
from .models import job

def home(request):
    Job=job.objects
    return render(request,'jobs/home.html',{'jobs':Job})
