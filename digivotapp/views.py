from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView,FormMixin
from django.template.context_processors import csrf
from django.db.models import Q
from django.contrib import messages

# from .models import AdminUserR
from .models import ManagerUserR,ElectionType,VoterReg
from .models import PoliticalCandidate,PoliticalParty
from .models import Ballot

from .forms import RegisterVoter,RegisterManager,Elections
from .forms import PartyForm, CandidateForm
from .forms import Confirm,VoterLogin


# Create your views here.
def home(request):  
    # context = {
    #     'voters': VoterReg.objects.all()
    # }
    # if request.method == 'POST' :
    #     form = VoterLogin(request.POST)
    #     if form.is_valid():
    #         return render(request,'adminElections.html')

    return render(request, 'index.html')

def managerLogin(request):
    return render(request,'managerLogin.html')

def managerVerifyPIN(request):
    return render(request,'managerVerifyPIN.html')

def managerRegister(request):
    return render(request,'managerRegister.html')

def adminLogin(request):
    context = {
        "name": "Sadsap",
    }
    template_name='adminLogin.html'
    return render(request,template_name, context)

def adminRegisterverifyPIN(request):
    context = {
        #'adminUser': AdminUserR.objects.all()
    }
    return render(request,'adminRegisterverifyPIN.html', context)

def adminRegister1(request):
    return render(request,'adminRegister1.html')

def adminRegister2(request):
    return render(request,'adminRegister2.html')

def adminPoliticalpartiesview(request):
    return render(request,'adminPoliticalpartiesview.html')

# def adminPoliticalpartiesadd(request):
#     return render(request, 'adminPoliticalpartiesadd.html')

def adminPoliticalpartiesedit(request):
    return render(request, 'adminPoliticalpartiesedit.html')

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
        context["count"] = ManagerUserR.objects.count()
        context["countV"] = VoterReg.objects.count()
        return context

class adminManagersaddmanager(CreateView):
    model = ManagerUserR
    form_class = RegisterManager
    template_name = 'adminManagersaddmanager.html'
    
    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request,'Your Manager has been created!')
        return redirect('adminManagerscreated')


class adminManagersview(DetailView):
    template_name = 'adminManagersview.html'
    model = ManagerUserR
    context_object_name = 'manager'

class adminEditmanagers(UpdateView):
    model = ManagerUserR
    template_name = 'adminManagersedit.html'
    fields = ['firstname','othername','lastname','phonenumber','email','DOB','gender','address','pictures']

    def get_success_url(self):
        return reverse('adminManagersview', kwargs={
            'pk': self.object.pk,
        })

class test(UpdateView):
    model = VoterReg
    template_name = 'adminManagersedit.html'
    fields = ['firstname','othername','lastname','phonenumber','email','DOB','status','title','statesoforigin','regionoforigin','statesofresidence','regionofresidence','nationality','religion','profession','address','pictures']

class adminManagersdelete(DeleteView):
    model = ManagerUserR
    template_name = 'adminManagersdelete.html'
    success_url = '/adminManagerscreated'

class adminElections(ListView):
    template_name = 'adminElections.html'
    model = ElectionType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["elections"] = ElectionType.objects.all().order_by('-dateadded')[:10]
        return context

class adminElectionsadd(SuccessMessageMixin ,CreateView):
    form_class = Elections
    template_name = 'adminElectionsadd.html'
    success_url = '/adminElections'
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

class adminElectionsdelete(DeleteView):
    model = ElectionType
    template_name = 'adminElectionsdelete.html'
    success_url = '/adminElections'


class adminPoliticalpartiesadd_party(SuccessMessageMixin ,CreateView):
    form_class = PartyForm
    template_name = 'adminPoliticalpartiesadd_party.html'
    success_url = '/adminPoliticalpartiesadd_candidate'
    success_message = "Party was created successfully"

class adminPoliticalpartiesadd_candidate(SuccessMessageMixin ,CreateView):
    form_class = CandidateForm
    template_name = 'adminPoliticalpartiesadd_candidate.html'
    success_url = '/adminPoliticalpartiesview'
    success_message = "Candidate was created successfully"

class adminPoliticalpartiesview(ListView):
    template_name = 'adminPoliticalpartiesview.html'
    model = PoliticalCandidate
    context_object_name = 'candidates'

class adminPoliticalpartiesedit_party(UpdateView):
    model = PoliticalParty
    template_name = 'adminPoliticalpartiesedit_party.html'
    fields = ['id','partyname','partyacronym','partysymbol']

    def form_valid(self,form):
        instance = form.save()
        return redirect('/adminPoliticalpartiesview')

class adminPoliticalpartiesedit_candidate(UpdateView):
    model = PoliticalCandidate
    template_name = 'adminPoliticalpartiesedit_candidate.html'
    fields = ['partyID','electionID','state','district','candidate_firstname','candidate_othername','candidate_surname',
    'candidate_age','candidate_nationality','candidate_educationalhistory','candidate_additionaldetails',
    'runningmate_firstname','runningmate_othername','runningmate_surname','runningmate_age','runningmate_nationality',
    'runningmate_educationalhistory','runningmate_additionaldetails']

    def form_valid(self,form):
        instance = form.save()
        
        return redirect('/adminPoliticalpartiesview')

class adminPoliticalpartydelete(DeleteView):
    model = PoliticalParty
    template_name = 'adminPoliticalpartydelete.html'
    success_url = '/adminPoliticalpartiesview'

class adminPoliticalcandidatedelete(DeleteView):
    model = PoliticalCandidate
    template_name = 'adminPoliticalcandidatedelete.html'
    success_url = '/adminPoliticalpartiesview'

class managerDash(ListView):
    template_name = 'managerDash.html'
    model = VoterReg

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voters"] = VoterReg.objects.all().order_by('-dateadded')[:10]
        context["count"] = ManagerUserR.objects.count()
        return context

class managerVoter(ListView):
    template_name = 'managerVoter.html'
    model = VoterReg

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voters"] = VoterReg.objects.all().order_by('-dateadded')[:10]
        return context

class managerVoteradd(SuccessMessageMixin ,CreateView):
    form_class = RegisterVoter
    template_name = 'managerVoteradd.html'
    success_url= '/managerVoter'
    success_message = "Voter registered successfully"

class managerViewvoter(DetailView):
    template_name = 'managerViewvoter.html'
    model = VoterReg
    context_object_name = 'voter'

class managerVoteredit(UpdateView):
    model = VoterReg
    template_name = 'managerVoteredit.html'
    fields = ['firstname','othername','lastname','phonenumber','email','DOB','status','title','statesoforigin','regionoforigin','statesofresidence','regionofresidence','nationality','religion','profession','address','pictures']

    def get_success_url(self):
        return reverse('managerViewvoter', kwargs={
            'pk': self.object.pk,
        })

class managerDeletevoter(DeleteView):
    model = VoterReg
    template_name = 'managerDeletevoter.html'
    success_url = '/managerVoter'

class managerCandidates(ListView):
    template_name = 'managerCandidates.html'
    model = PoliticalCandidate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["candidates"] = PoliticalCandidate.objects.all().order_by('-dateadded')[:10]
        #context["count"] = ManagerUserR.objects.count()
        return context

def managerRequests(request):
    return render(request, 'managerRequests.html')

def resultDetails(request):
    return render(request, 'resultDetails.html')

class votersLanding(ListView):
    template_name = 'votersLanding.html'
    model = PoliticalCandidate
    context_object_name = 'candidates'

def load_regions(request):
    state_id = request.GET.get('state')
    regions = Region.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'hr/region_dropdown_list_options.html', {'regions': regions })

def adminSearchformanager(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = ManagerUserR.objects.filter(
            Q(firstname__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(gender__icontains=search_term) |
            Q(phonenumber__iexact=search_term)
            )
        context = {
            'search_term': search_term,
            'managers': search_results
        }
        return render(request, 'adminSearchformanager.html', context)
    else:
        return redirect('adminManagerscreated')

def adminSearchforelection(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = ElectionType.objects.filter(
            Q(electiontitle__icontains=search_term) |
            Q(electiontype__icontains=search_term) |
            Q(requiredposition__icontains=search_term)
        )
        context = {
                'search_term': search_term,
                'elections': search_results
        }
        return render(request, 'adminSearchforelection.html', context)
    else:
        return redirect('adminElection')

def adminSearchforparty(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = PoliticalParty.objects.filter(
            Q(partyname__icontains=search_term) |
            Q(partyacronym__icontains=search_term)
        )
        context = {
                'search_term': search_term,
                'parties': search_results,
        }
        return render(request, 'adminSearchforparty.html', context)
    else:
        return redirect('adminElection')

def adminSearchforcandidate(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = PoliticalCandidate.objects.filter(
            Q(candidate_firstname__icontains=search_term) |
            Q(runningmate_firstname=search_term)
            )
        context = {
            'search_term': search_term,
            'candidates': search_results
        }
        return render(request, 'adminSearchforcandidate.html', context)
    else:
        return redirect('managerCandidates')

# class confirmVote(DetailView):
#     # form_class = CandidateForm
#     template_name = 'confirmVote.html'
#     # success_url= '/voterLanding'
#     model = PoliticalCandidate
#     context_object_name = 'candidate'

def confirmVote(request,pk):
    context = {}

    context["candidate"] = PoliticalCandidate.objects.get(id = pk)

    # if request.method == "POST":
    #     form = Confirm(request.POST) 

    # if form.is_valid(): 
    #     form.save() 
    #     messages.success(request,'Vote successfully cast')
    #     return render(request,"index.html")
    form = Confirm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Vote successfully cast')
        return render(request,"index.html")
    
    context['form'] = form 
    return render(request, "confirmVote.html", context)