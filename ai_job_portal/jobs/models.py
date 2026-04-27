# jobs/models.py

from django.db import models
from django.contrib.auth.models import User


# ---------------- JOB MODEL ----------------
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    skills_required = models.TextField(help_text="Enter skills separated by commas")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ---------------- APPLICATION MODEL ----------------
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} applied to {self.job.title}"