from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
 
urlpatterns = [
    path('', views.home, name="home"),
    # url(r'^accounts/', include('allauth.urls')),

    path('managerLogin/', views.managerLogin, name="managerLogin"),
    path('managerDash/', views.managerDash.as_view(), name="managerDash"),
    path('managerVerifyPIN/', views.managerVerifyPIN, name="managerVerifyPIN"),
    path('managerRegister/', views.managerRegister, name="managerRegister"),
    path('adminLogin/', views.adminLogin, name="adminLogin"),
    path('adminRegisterverifyPIN/', views.adminRegisterverifyPIN, name="adminRegisterverifyPIN"),
    path('adminRegister1/', views.adminRegister1, name="adminRegister1"),
    path('adminRegister2/', views.adminRegister2, name="adminRegister2"),
    path('adminDash/', views.adminDash.as_view(), name="adminDash"),
    path('adminManagerscreated/', views.adminManagerscreated.as_view(), name="adminManagerscreated"),
    path('adminPoliticalpartiesview/', views.adminPoliticalpartiesview.as_view(), name="adminPoliticalpartiesview"),
    path('adminPoliticalpartiesadd_party/',views.adminPoliticalpartiesadd_party.as_view(), name="adminPoliticalpartiesadd_party"),
    path('adminPoliticalpartiesadd_candidate/',views.adminPoliticalpartiesadd_candidate.as_view(), name="adminPoliticalpartiesadd_candidate"),
    path('adminPoliticalpartiesedit_party/<int:pk>/',views.adminPoliticalpartiesedit_party.as_view(), name="adminPoliticalpartiesedit_party"),
    path('adminPoliticalpartydelete/<int:pk>/',views.adminPoliticalpartydelete.as_view(), name="adminPoliticalpartydelete"),
    path('adminPoliticalpartiesedit_candidate/<int:pk>/',views.adminPoliticalpartiesedit_candidate.as_view(), name="adminPoliticalpartiesedit_candidate"),
    path('adminPoliticalcandidatedelete/<int:pk>/',views.adminPoliticalcandidatedelete.as_view(), name="adminPoliticalcandidatedelete"),
    path('adminElections/', views.adminElections.as_view(), name="adminElections"),
    path('addElections/', views.adminElectionsadd.as_view(), name="adminElectionsadd"),
    path('adminElections/editElections/<int:pk>/', views.adminElectionsedit.as_view(), name="adminElectionsedit"),
    path('adminElections/viewElections/<int:pk>/', views.adminElectionsview.as_view(), name="adminElectionsview"),
    path('adminElections/deleteElections/<int:pk>/', views.adminElectionsdelete.as_view(), name="adminElectionsdelete"),
    path('adminManagersaddmanager/', views.adminManagersaddmanager.as_view(), name="adminManagersaddmanager"),
    path('adminManagerscreated/viewmanager/<int:pk>/', views.adminManagersview.as_view(), name="adminManagersview"),
    path('adminEditmanagers/<int:pk>/', views.adminEditmanagers.as_view(),name="adminEditmanagers"),
    path('adminManagerscreated/deletemanager/<int:pk>/', views.adminManagersdelete.as_view(), name="adminManagersdelete"),
    path('adminPoliticalpartiesedit/', views.adminPoliticalpartiesedit, name="adminPoliticalpartiesedit"),
    path('managerVoter/', views.managerVoter.as_view(), name="managerVoter"),
    path('ViewVoterDetails/<int:pk>/',views.managerViewvoter.as_view(),name="managerViewvoter"),
    path('managerVoter/deletemanager/<int:pk>/', views.managerDeletevoter.as_view(), name="managerDeletevoter"),
    path('managerVoter/registerVoter/', views.managerVoteradd.as_view(), name="managerVoteradd"),
    path('managerRequests/', views.managerRequests, name="managerRequests"),
    path('managerCandidates/', views.managerCandidates.as_view(), name="managerCandidates"),
    path('EditVoterDetails/<int:pk>/', views.managerVoteredit.as_view(), name="managerVoteredit"),
    path('resultDetails/', views.resultDetails, name="resultDetails"),
    path('votersLanding/', views.votersLanding.as_view(), name="votersLanding"),
    path('searchManagers/', views.adminSearchformanager, name="adminSearchformanager"),
    path('searchElections/', views.adminSearchforelection, name="adminSearchforelection"), 
    path('searchParties/', views.adminSearchforparty, name="adminSearchforparty"),
    path('searchCandidates/', views.adminSearchforcandidate, name="adminSearchforcandidate"), 
    path('ajax/load-regions/', views.load_regions, name='ajax_load_regions'),
    path('confirmVote/<int:pk>/', views.confirmVote, name='confirmVote'),

    # path('test/', views.test.as_view(),"test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)