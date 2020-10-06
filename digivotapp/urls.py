from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from . import views
 
urlpatterns = [
    path('', views.reroute_, name='landing_page'),
    path('admin/dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin/managers/add/', views.admin_add_manager, name="admin_add_manager"),
    path('admin/managers/view/', views.AdminViewManagers.as_view(), name="admin_view_managers"),
    path('admin/managers/view/<int:pk>/', views.admin_view_manager, name="admin_view_a_manager"),
    path('admin/managers/edit/<int:pk>/', views.admin_edit_manager, name="admin_edit_manager"),
    path('admin/managers/delete/<int:pk>/', views.admin_delete_manager, name="admin_delete_manager"),
    path('admin/managers/search/', views.admin_manager_search, name="admin_manager_search"),
    path('adminR/', views.adminRegister, name="adminReg"),

    path('adminPoliticalpartiesview/', views.adminPoliticalpartiesview.as_view(), name="adminPoliticalpartiesview"),
    path('adminPoliticalpartiesadd_party/', views.adminPoliticalpartiesadd_party.as_view(), name="adminPoliticalpartiesadd_party"),
    path('adminPoliticalpartiesadd_candidate/', views.adminPoliticalpartyadd_candidate.as_view(), name="adminPoliticalpartiesadd_candidate"),
    path('adminPoliticalpartiesedit_party/<int:pk>/',views.adminPoliticalpartiesedit_party.as_view(), name="adminPoliticalpartiesedit_party"),
    path('adminPoliticalpartydelete/<int:pk>/',views.adminPoliticalpartdelete.as_view(), name="adminPoliticalpartydelete"),
    path('adminPoliticalpartiesedit_candidate/<int:pk>/',views.adminPoliticalpartiesedit_candidate.as_view(), name="adminPoliticalpartiesedit_candidate"),
    path('adminPoliticalcandidatedelete/<int:pk>/',views.adminPoliticalcandidatedelete.as_view(), name="adminPoliticalcandidatedelete"),
    path('adminElections/', views.adminElections.as_view(), name="adminElections"),
    path('addElections/', views.adminElectionadd.as_view(), name="adminElectionsadd"),
    path('adminElections/editElections/<int:pk>/', views.adminElectionsedit.as_view(), name="adminElectionsedit"),
    path('adminElections/viewElections/<int:pk>/', views.adminElectionsview.as_view(), name="adminElectionsview"),
    path('adminElections/deleteElections/<int:pk>/', views.admindeleteElection.as_view(), name="adminElectionsdelete"),

    path('adminPoliticalpartiesedit/', views.adminPoliticalpartiesedit, name="adminPoliticalpartiesedit"),
    path('manager/dashboard/', views.ManagerDashboard.as_view(), name="managerDash"),
    path('managerVoter/', views.managerVoter.as_view(), name="managerVoter"),
    # path('ViewVoterDetails/<int:pk>/',views.managerViewvoter.as_view(),name="managerViewvoter"),
    # path('managerVoter/deletemanager/<int:pk>/', views.managerDeletevoter.as_view(), name="managerDeletevoter"),
    path('managerVoter/registerVoter/', views.managerVoteradd.as_view(), name="managerVoteradd"),
    path('managerRequests/', views.managerRequests, name="managerRequests"),
    path('managerCandidates/', views.managerCandidates.as_view(), name="managerCandidates"),
    # path('EditVoterDetails/<int:pk>/', views.managerVoteredit.as_view(), name="managerVoteredit"),
    path('resultDetails/', views.resultDetails, name="resultDetails"),
    path('votersLanding/', views.votersLanding.as_view(), name="votersLanding"),
    path('searchElections/', views.adminSearchforelection, name="adminSearchforelection"),
    path('searchParties/', views.adminSearchforparty, name="adminSearchforparty"),
    path('searchCandidates/', views.adminSearchforcandidate, name="adminSearchforcandidate"),
    path('ajax/load-regions/', views.load_regions, name='ajax_load_regions'),
    path('confirmVote/<int:pk>/', views.confirmVote, name='confirmVote'),
    path('displayResults/', views.display_result, name='displayResults'),
    path('displayResults/<int:election_id>/', views.display_result, name='displayResults'),

]
