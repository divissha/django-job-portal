from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

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

    def __str__(self):
        return self.applicant_name