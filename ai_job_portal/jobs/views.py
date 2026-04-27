# jobs/views.py

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Application


# ---------------- APPLY JOB ----------------
@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # Prevent duplicate application
    already_applied = Application.objects.filter(user=request.user, job=job).exists()

    if not already_applied:
        Application.objects.create(user=request.user, job=job)

    return redirect('dashboard')