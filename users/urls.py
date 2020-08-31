from django.urls import path
from . import views

urlpatterns = [
    path('register/<str:permission>/', views.new_user_register, name='user_register'),
    path('login/', views.new_user_register, name='user_login'),
]

"""
manager_voter_add- voter
adminmanageraddmanager - manager
adminregister
"""