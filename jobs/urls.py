from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'apply/<int:job_id>/',
        views.apply_job,
        name='apply_job'
    ),

    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='jobs/login.html'
    ),
    name='login'
    ),
    
    path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
    ),
    
    path(
    'register/',
    views.register,
    name='register'
    ),

    path(
    'my-applications/',
    views.my_applications,
    name='my_applications'
    ),
]