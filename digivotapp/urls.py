from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('adminRegister2/', views.adminRegister2, name="adminRegister2"),
    path('managerLogin/', views.managerLogin, name="managerLogin"),
    path('managerDash/', views.dashboardMan, name="managerDash"),
    path('managerVerifyPIN/', views.managerVerifyPIN, name="managerVerifyPIN"),
    path('managerRegister/', views.managerRegister, name="managerRegister"),
    path('adminLogin/', views.adminLogin, name="adminLogin"),
    path('adminRegisterverifyPIN/', views.adminRegisterverifyPIN, name="adminRegisterverifyPIN"),
    path('adminRegister1/', views.adminRegister1, name="adminRegister1"),
    path('adminDash/', views.adminDash.as_view(), name="adminDash"),
    path('adminManagerscreated/', views.adminManagerscreated.as_view(), name="adminManagerscreated"),
    path('adminPoliticalpartiesview/', views.adminPoliticalpartiesview, name="adminPoliticalpartiesview"),
    path('adminElections/', views.adminElections.as_view(), name="adminElections"),
    path('addElections/', views.adminElectionsadd.as_view(), name="adminElectionsadd"),
    path('adminElections/editElections/<int:pk>', views.adminElectionsedit.as_view(), name="adminElectionsedit"),
    path('adminElections/viewElections/<int:pk>', views.adminElectionsview.as_view(), name="adminElectionsview"),
    path('adminManagersregistered/', views.adminManagersregistered, name="adminManagersregistered"),
    path('adminManagersaddmanager/', views.adminManagersaddmanager.as_view(), name="adminManagersaddmanager"),
    path('adminManagerseditmanager/', views.adminManagerseditmanager, name="adminManagerseditmanager"),
    path('adminManagersviewmanager/', views.adminManagersviewmanager, name="adminManagersviewmanager"),
    path('adminPoliticalpartiesadd/', views.adminPoliticalpartiesadd, name="adminPoliticalpartiesadd"),
    path('adminPoliticalpartiesedit/', views.adminPoliticalpartiesedit, name="adminPoliticalpartiesedit"),
    path('managerDash/', views.managerDash, name="managerDash"),

    path('managerVoter/', views.managerVoter.as_view(), name="managerVoter"),
    path('ViewVoterDetails/<int:pk>/',views.managerVoterview.as_view(),name="managerVoterview"),

    path('managerRequests/', views.managerRequests, name="managerRequests"),
    path('managerCandidates/', views.managerCandidates, name="managerCandidates"),
    path('RegisterVoter/', views.managerVoteradd, name="managerVoteradd"),
    path('EditVoterDetails/', views.managerVoteredit, name="managerVoteredit"),
    path('resultDetails/', views.resultDetails, name="resultDetails"),
    path('votersLanding/', views.votersLanding, name="votersLanding"),
]