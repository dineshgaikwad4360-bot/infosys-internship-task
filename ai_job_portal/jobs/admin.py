# jobs/admin.py

from django.contrib import admin
from .models import Job, Application
from django.contrib import admin
from .models import Job, Application


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'created_at')
    search_fields = ('title', 'company')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'applied_at')
    search_fields = ('user__username', 'job__title')


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)


