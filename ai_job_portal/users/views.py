# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Profile
from jobs.models import Job, Application


# ---------------- REGISTER ----------------
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('login')

    return render(request, 'register.html')


# ---------------- LOGIN ----------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# ---------------- LOGOUT ----------------
def user_logout(request):
    logout(request)
    return redirect('login')


# ---------------- AI MATCH FUNCTION ----------------
def match_score(user_skills, job_skills):
    user_set = set(user_skills.lower().replace(" ", "").split(','))
    job_set = set(job_skills.lower().replace(" ", "").split(','))

    matched = user_set.intersection(job_set)
    return len(matched)


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    jobs = Job.objects.all()

    # Get user skills
    try:
        profile = Profile.objects.get(user=request.user)
        user_skills = profile.skills
    except:
        user_skills = ""

    job_list = []

    for job in jobs:
        score = match_score(user_skills, job.skills_required)
        job_list.append((job, score))

    # Sort by best match
    job_list.sort(key=lambda x: x[1], reverse=True)

    # Get applied jobs
    applied_jobs = Application.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'job_list': job_list,
        'applied_jobs': applied_jobs
    })