from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.applicant_name