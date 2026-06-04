from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .models import Application
from .forms import ApplicationForm

# def home(request):
#     return HttpResponse("Welcome to my Job Portal!")

def home(request):
    return render(request, 'jobs/home.html')

def home(request):
    jobs = Job.objects.all()

    return render(
        request,
        'jobs/home.html',
        {'jobs': jobs}
    )

def apply_job(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    if request.method == 'POST':

        form = ApplicationForm(
            request.POST
        )

        if form.is_valid():

            application = form.save(
                commit=False
            )

            application.job = job

            application.save()

            return redirect('/')

    else:

        form = ApplicationForm()

    return render(
        request,
        'jobs/apply.html',
        {
            'form': form,
            'job': job
        }
    )