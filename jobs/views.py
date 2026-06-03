from django.shortcuts import render

from django.http import HttpResponse
from .models import Job

def home(request):
    return HttpResponse("Welcome to my Job Portal!")

def home(request):
    return render(request, 'jobs/home.html')

def home(request):
    jobs = Job.objects.all()

    return render(
        request,
        'jobs/home.html',
        {'jobs': jobs}
    )