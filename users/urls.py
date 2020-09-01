from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='user_login'),
    path('register/', views.new_user_register, name='user_register'),
    path('validate/', views.move_auth_browser, name='validate_user'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
