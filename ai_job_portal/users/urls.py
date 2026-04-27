from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='home'),   # 👈 ADD THIS LINE
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]