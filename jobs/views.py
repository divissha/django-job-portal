from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .models import Application
from .forms import ApplicationForm

from django.contrib.auth import login
from .auth_forms import RegisterForm

from django.contrib.auth.decorators import login_required

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

@login_required
def my_applications(request):

    applications = Application.objects.filter(
        user=request.user
    )

    return render(
        request,
        'jobs/my_applications.html',
        {
            'applications': applications
        }
    )

@login_required
def apply_job(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    if request.method == 'POST':

        form = ApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save(
                commit=False
            )

            application.job = job
            application.user = request.user
            application.applicant_name = request.user.username
            application.email = request.user.email
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

def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(
        request,
        'jobs/register.html',
        {'form': form}
    )

def home(request):
    jobs = Job.objects.all()
    return render(
    request,
    'jobs/home.html',
    {
        'jobs': jobs,
        'job_count': jobs.count()
    }
)