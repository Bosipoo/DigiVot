from django import forms
from django.utils.timezone import datetime
from django.forms import ModelForm
from .models import Region, ElectionType, PoliticalParty, PoliticalCandidate, Ballot
from bootstrap_modal_forms.forms import BSModalModelForm

this_year = datetime.now().year
next_year = this_year + 1
start_year = this_year - 18
end_year = this_year - 80

    
class Elections(forms.ModelForm):
    class Meta:
        model = ElectionType
        fields = ['electionID','electiontitle','electiontype','registeration_start','registeration_end','voting_start','voting_end','requiredposition']
        widgets = {
            'registeration_start':forms.SelectDateWidget(years=range(next_year, this_year)),
            'registeration_end':forms.SelectDateWidget(years=range(next_year, this_year)),
            'voting_start':forms.SelectDateWidget(years=range(next_year, this_year)),
            'voting_end':forms.SelectDateWidget(years=range(next_year, this_year))
            }


class PartyForm(forms.ModelForm):
    class Meta:
        model = PoliticalParty
        fields = ['partyname','partyacronym','partysymbol']


class CandidateForm(forms.ModelForm):
    class Meta:
        model = PoliticalCandidate
        fields = ['id','partyID','electionID','state','district','candidate_firstname','candidate_othername','candidate_surname',
        'candidate_age','candidate_nationality','candidate_educationalhistory','candidate_additionaldetails',
        'runningmate_firstname','runningmate_othername','runningmate_surname','runningmate_age','runningmate_nationality',
        'runningmate_educationalhistory','runningmate_additionaldetails']


class Confirm(forms.ModelForm):
    class Meta:
        model = Ballot
        fields = ['voteID','candidateID']
