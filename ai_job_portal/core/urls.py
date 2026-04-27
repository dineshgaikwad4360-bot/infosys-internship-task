# core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users app (login, register, dashboard)
    path('', include('users.urls')),

    # Jobs app (apply job)
    path('', include('jobs.urls')),
]