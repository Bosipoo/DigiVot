from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import AdminUserR
from .models import VoterReg
from .models import ManagerUserR
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

def adminElections(request):
    return render(request,'adminElections.html')

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

def adminManagerscreated(request):
    return render(request,'')

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
