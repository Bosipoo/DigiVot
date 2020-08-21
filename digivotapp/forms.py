from django import forms
from django.utils.timezone import datetime
from django.forms import ModelForm
from .models import VoterReg,Region,ManagerUserR,ElectionType,PoliticalParty,PoliticalCandidate,Ballot
from bootstrap_modal_forms.forms import BSModalModelForm

# class PinForm(forms.Form):
#     pin = forms.CharField(label='PIN',max_length=100)
#     # def clean(self):
#     #     data = super(PinForm,self).clean()
#     #     pin = cleaned_data.get("pin")
#     #     try:
#     #         p = AdminUserR.objects.get(id=Pin)
#     #     except AdminUserR.DoesNotExist:
#     #         raise forms.ValidationError("User does not exist.")

this_year = datetime.now().year
next_year = this_year + 1
start_year = this_year - 18
end_year = this_year - 80

class RegisterVoter(forms.ModelForm):
    class Meta:
        model = VoterReg
        fields = ['firstname','othername','lastname','phonenumber','email','DOB','status','title','state','region',
                  'statesofresidence','regionofresidence','nationality','religion','profession','address','pictures']
        widgets = {'DOB':forms.SelectDateWidget(years=range(end_year, start_year))}
    

class RegisterManager(forms.ModelForm):
    class Meta:
        model = ManagerUserR
        fields = ['firstname','othername','lastname','phonenumber','email','DOB','gender','address','pictures']
        widgets = {'DOB':forms.SelectDateWidget(years=range(end_year, start_year))}
    
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

class VoterLogin(forms.ModelForm):
    class Meta:
        model = VoterReg
        fields = ('pin',)       

    # def clean_pin(self):
    #     pin = self.cleaned_data.get('pin',False)
    #     if not self.instance.pin == pin:
    #         raise forms.ValidationError("Unregistered Voter")
    #     return None