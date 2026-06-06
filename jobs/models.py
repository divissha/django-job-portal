from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(
    max_length=100,
    default='Remote'
    )

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()

    resume = models.FileField(
        upload_to='resumes/',
        null=True,
        blank=True
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Reviewed', 'Reviewed'),
    ('Rejected', 'Rejected'),
    ('Accepted', 'Accepted')
    ]
    
    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='Pending'
    )

    def __str__(self):
        return self.applicant_name
    
    
    
