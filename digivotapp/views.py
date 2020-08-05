from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import AdminUserR
from .models import VoterReg
from .models import ManagerUserR,ElectionType
from django.views.generic.edit import FormView

# Create your views here.
def home(request):
    return render(request,'index.html')

def managerLogin(request):
    return render(request,'managerLogin.html')

def managerVerifyPIN(request):
    return render(request,'managerVerifyPIN.html')

def managerRegister(request):
    return render(request,'managerRegister.html')

def dashboardMan(request):
    context = {
        'names': 'I beg you'
    }
    template_name = 'managerDash.html'
    return render(request,template_name)

def adminLogin(request):
    context = {
        "name": "Sadsap",
    }
    template_name='adminLogin.html'
    return render(request,template_name, context)

def adminRegisterverifyPIN(request):
    context = {
        'adminUser': AdminUserR.objects.all()
    }
    return render(request,'adminRegisterverifyPIN.html', context)

def adminRegister1(request):
    return render(request,'adminRegister1.html')

def adminRegister2(request):
    return render(request,'adminRegister2.html')

def adminPoliticalpartiesview(request):
    return render(request,'adminPoliticalpartiesview.html')

def adminManagersregistered(request):
    return render(request,'adminManagersregistered.html')

def adminManagersaddmanager(request):
    return render(request,'adminManagersaddmanager.html')

def adminManagersaddmanager(request):
    return render(request,'adminManagersaddmanager.html')

def adminManagerseditmanager(request):
    return render(request,'adminManagerseditmanager.html')

def adminManagersviewmanager(request):
    return render(request,'adminManagersviewmanager.html')

def adminPoliticalpartiesadd(request):
    return render(request, 'adminPoliticalpartiesadd.html')

def adminPoliticalpartiesedit(request): 
    return render(request, 'adminPoliticalpartiesedit.html')

def managerDash(request):
    return render(request, 'managerDash.html')

class adminDash(ListView):
    template_name = 'adminDash.html'
    model = ManagerUserR

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["managers"] = ManagerUserR.objects.all().order_by('-dateadded')[:10]
        return context

class adminManagerscreated(ListView):
    template_name = 'adminManagerscreated.html'   
    model = ManagerUserR

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["managers"] = ManagerUserR.objects.all().order_by('-dateadded')[:10]
        return context

class adminManagersaddmanager(SuccessMessageMixin ,CreateView):
    model = ManagerUserR
    template_name = 'adminManagersaddmanager.html'
    fields = ['firstname','othername','lastname','phonenumber','email','DOB','gender','address','pictures']
    success_url = '/adminManagerscreated'
    success_message = "%(email)s was created successfully"

# class adminElectionslistandview(CreateView):
#     model = ElectionType
#     template_name = 'adminElections.html'

#     fields = ['electiontitle','electiontype','registeration_start','registeration_end','voting_start','voting_end','requiredposition'] 
#     # success_url = '/adminElections.html'
#     # success_message = "%(email)s was created successfully"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["objects"] = self.model.objects.all()
#         return context

class adminElections(ListView):
    template_name = 'adminElections.html'
    model = ElectionType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["elections"] = ElectionType.objects.all().order_by('-dateadded')[:10]
        return context

class adminElectionsadd(SuccessMessageMixin ,CreateView):
    model = ElectionType
    template_name = 'adminElectionsadd.html'
    fields = ['electionID','electiontitle','electiontype','registeration_start','registeration_end','voting_start','voting_end','requiredposition']
    success_url = '/addElections'
    success_message = "Election was created successfully"

class adminElectionsedit(UpdateView):
    model = ElectionType
    template_name = 'adminElectionsedit.html'
    fields = ['electionID','electiontitle','electiontype','registeration_start','registeration_end','voting_start','voting_end','requiredposition']

    def form_valid(self,form):
        instance = form.save()
        return redirect('adminElections')

class adminElectionsview(DetailView):
    template_name = 'adminElectionsview.html'
    model = ElectionType
    context_object_name = 'election'

class managerVoter(ListView):
    template_name = 'managerVoter.html'
    model = VoterReg

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voters"] = VoterReg.objects.all().order_by('-dateadded')[:10]
        return context

class managerVoterview(DetailView):
    template_name= 'managerVoterview.html'
    model = VoterReg
    context_object_name = 'voter'


def managerRequests(request):
    return render(request, 'managerRequests.html')

def managerCandidates(request):
    return render(request, 'managerCandidates.html')

def managerVoteradd(request):
    return render(request, 'managerVoteradd.html')

def managerVoteredit(request):
    return render(request, 'managerVoteredit.html')



def resultDetails(request):
    return render(request, 'resultDetails.html')

def votersLanding(request):
    return render(request, 'votersLanding.html')
