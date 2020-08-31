from django.urls import path
from . import views

urlpatterns = [
    path('register/<str:permission>/', views.new_user_register, name='user_register'),
    path('login/', views.new_user_register, name='user_login'),
    path('validate/', views.move_auth_browser, name='validate_user'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]

"""
manager_voter_add- voter
adminmanageraddmanager - manager
adminregister
"""