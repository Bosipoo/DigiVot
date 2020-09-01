from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView, FormMixin
from django.template.context_processors import csrf
from django.db.models import Q
from django.contrib import messages

# from .models import AdminUserR
from .models import ElectionType
from .models import PoliticalCandidate, PoliticalParty
from .models import Ballot, Region

from .forms import Elections
from .forms import PartyForm, CandidateForm
from .forms import Confirm
from users.models import CustomUser,Profile


#Create your views here.
def home(request):
    # context = {
    #     'voters': VoterReg.objects.all()
    # }
    if request.method == 'POST':
        return redirect('votersLanding')

    return render(request, 'index.html')


def managerLogin(request):
    return render(request, 'managerLogin.html')


def managerVerifyPIN(request):
    return render(request, 'managerVerifyPIN.html')


def managerRegister(request):
    return render(request, 'managerRegister.html')


def adminLogin(request):
    context = {
        "name": "Sadsap",
    }
    template_name = 'adminLogin.html'
    return render(request, template_name, context)


def adminRegisterverifyPIN(request):
    context = {
        # 'adminUser': AdminUserR.objects.all()
    }
    return render(request, 'adminRegisterverifyPIN.html', context)


def adminRegister1(request):
    return render(request, 'adminRegister1.html')


def adminRegister2(request):
    return render(request, 'adminRegister2.html')


def adminPoliticalpartiesview(request):
    return render(request, 'adminPoliticalpartiesview.html')


def adminPoliticalpartiesadd(request):
    return render(request, 'adminPoliticalpartiesadd.html')


def adminPoliticalpartiesedit(request):
    return render(request, 'adminPoliticalpartiesedit.html')


class adminDash(ListView):
    template_name = 'adminDash.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["partydisplays"] = PoliticalParty.objects.all()
        #context["managers"] = CustomUser.objects.filter(is_manager=True).order_by('-dateadded')[:10]
        return context


class adminManagerscreated(ListView):
    template_name = 'adminManagerscreated.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["managers"] = CustomUser.objects.filter(is_manager=True)[:10]
        context["count"] = CustomUser.objects.filter(is_manager=True).count()
        context["countV"] = CustomUser.objects.filter(is_voter=True).count()
        return context

class adminManagersdelete(DeleteView):
    model = CustomUser
    template_name = 'adminManagersdelete.html'
    success_url = '/adminManagerscreated'


class adminElections(ListView):
    template_name = 'adminElections.html'
    model = ElectionType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["elections"] = ElectionType.objects.all().order_by('-dateadded')[:10]
        return context

class adminElectionsadd(SuccessMessageMixin, CreateView):
    form_class = Elections
    template_name = 'adminElectionsadd.html'
    success_url = '/adminElections'
    success_message = "Election was created successfully"

class adminElectionsedit(UpdateView):
    model = ElectionType
    template_name = 'adminElectionsedit.html'
    fields = ['electionID', 'electiontitle', 'electiontype', 'registeration_start', 'registeration_end', 'voting_start',
              'voting_end', 'requiredposition']

    def form_valid(self, form):
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

class adminPoliticalpartiesadd_party(SuccessMessageMixin, CreateView):
    form_class = PartyForm
    template_name = 'adminPoliticalpartiesadd_party.html'
    success_url = '/adminPoliticalpartiesadd_candidate'
    success_message = "Party was created successfully"

class adminPoliticalpartiesadd_candidate(SuccessMessageMixin, CreateView):
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
    fields = ['id', 'partyname', 'partyacronym', 'partysymbol']

    def form_valid(self, form):
        instance = form.save()
        return redirect('/adminPoliticalpartiesview')

class adminPoliticalpartiesedit_candidate(UpdateView):
    model = PoliticalCandidate
    template_name = 'adminPoliticalpartiesedit_candidate.html'
    fields = ['partyID', 'electionID', 'state', 'candidate_firstname', 'candidate_othername',
              'candidate_surname',
              'candidate_age', 'candidate_nationality', 'candidate_educationalhistory', 'candidate_additionaldetails',
              'runningmate_firstname', 'runningmate_othername', 'runningmate_surname', 'runningmate_age',
              'runningmate_nationality',
              'runningmate_educationalhistory', 'runningmate_additionaldetails']

    def form_valid(self, form):
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
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voters"] = CustomUser.objects.filter(is_voter=True)[:10]
        context["count"] = CustomUser.objects.filter(is_manager=True).count()
        context["countV"] = CustomUser.objects.filter(is_voter=True).count()
        return context


class managerVoter(ListView):
    template_name = 'managerVoter.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voters"] = CustomUser.objects.filter(is_voter=True)[:10]
        return context


# class managerVoteradd(SuccessMessageMixin, CreateView):
#     form_class = RegisterVoter
#     template_name = 'managerVoteradd.html'
#     success_url = '/managerVoter'
#     success_message = "Voter registered successfully"


class managerViewvoter(DetailView):
    template_name = 'managerViewvoter.html'
    model = CustomUser
    context_object_name = 'voter'


class managerVoteredit(UpdateView):
    model = CustomUser
    template_name = 'managersEditvoter.html'
    fields = ['firstname', 'othername', 'lastname', 'phonenumber', 'email', 'DOB', 'status', 'title', 'state', 'region',
              'statesofresidence', 'regionofresidence', 'nationality', 'religion', 'profession', 'address', 'pictures']
    context_object_name = 'voter'

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, 'Your Manager has been updated!')
        return redirect('/managerDash')


# class managerDeletevoter(DeleteView):
#     model = VoterReg
#     template_name = 'managerDeletevoter.html'
#     success_url = '/managerVoter'
#     context_object_name = 'voter'

class managerCandidates(ListView):
    template_name = 'managerCandidates.html'
    model = PoliticalCandidate

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["candidates"] = PoliticalCandidate.objects.all().order_by('-dateadded')[:10]
        # context["count"] = ManagerUserR.objects.count()
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
    return render(request, 'hr/region_dropdown_list_options.html', {'regions': regions})

def adminSearchformanager(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = CustomUser.objects.filter(
            Q(firstname__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(gender__icontains=search_term) |
            Q(phonenumber__iexact=search_term), is_manager=True
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

def confirmVote(request, pk):
    context = {}

    context["candidate"] = PoliticalCandidate.objects.get(id=pk)
    form = Confirm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Vote successfully cast')
        return redirect('home')
        
    context['form'] = form
    return render(request, "confirmVote.html", context)


def display_result(request, election_id=None):
    if election_id:
        election = get_object_or_404(ElectionType, electionID=election_id)
        candidates = PoliticalCandidate.objects.filter(electionID=election)
        total_votes = Ballot.objects.filter(electionID=election)
        votes_breakdown = {}
        for candidate in candidates:
            votes_breakdown[candidate.id] = total_votes.filter(candidateID=candidate).count()

        return render(request,
                      'resultDetail.html',
                      {'election': election,
                       'candidates': candidates,
                       'total_votes': len(total_votes),
                       'votes_breakdown': votes_breakdown})
    else:
        elections = ElectionType.objects.all()
        votes = {}
        for election in elections:
            votes[election.electionID] = Ballot.objects.filter(electionID=election).count()
        return render(request, 'results.html', {'elections': elections,
                                                'votes_count': votes})
