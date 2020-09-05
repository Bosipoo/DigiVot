from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='user_login'),
    path('register/', views.new_user_register, name='user_register'),
    #path('validate/<str:key>/', views.login_to_browser, name='browser_login'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('users/logout/', views.account_logout, name='user_logout'),
]
