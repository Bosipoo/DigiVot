from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.timezone import now
from .widgets import BootstrapDateTimePickerInput
from .formatChecker import ContentTypeRestrictedFileField
import datetime
import string


# Create your models here.
class Super_Registeradmin(models.Model):
    pin = models.CharField(primary_key=True,
                           default="A" + get_random_string(4, allowed_chars=string.ascii_uppercase + string.digits),
                           max_length=5, editable=False)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Region(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# class District(models.Model):
#     region = models.ForeignKey(Region, on_delete=models.CASCADE)
#     district_name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.district_name


class PoliticalParty(models.Model):
    partyname = models.CharField(max_length=50)
    partyacronym = models.CharField(max_length=5)
    partysymbol = ContentTypeRestrictedFileField(upload_to='Images/', content_types=['image/jpeg', 'image/png', ],
                                                 max_upload_size=5242880, blank=True, null=True)

    def __str__(self):
        return self.partyname


class ElectionType(models.Model):
    electionID = models.AutoField(primary_key=True)
    electiontitle = models.CharField(max_length=50)
    electiontype = models.CharField(max_length=100, choices=(
        ('Presidential', 'Presidential'),
        ('Gubernatorial', 'Gubernatorial'),
        ('Senatorial', 'Senatoial')
    ), default='Presidential')
    registeration_start = models.DateField()
    registeration_end = models.DateField()
    voting_start = models.DateField()
    voting_end = models.DateField()
    requiredposition = models.TextField(max_length=200)
    dateadded = models.DateField(default=now)

    def __str__(self):
        return self.electiontitle


class PoliticalCandidate(models.Model):
    partyID = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE)
    electionID = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    #district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    candidate_firstname = models.CharField(max_length=50)
    candidate_othername = models.CharField(max_length=50)
    candidate_surname = models.CharField(max_length=50)
    candidate_age = models.IntegerField()
    candidate_nationality = models.CharField(max_length=50)
    candidate_educationalhistory = models.CharField(max_length=200)
    candidate_additionaldetails = models.TextField(max_length=200)
    runningmate_firstname = models.CharField(max_length=50)
    runningmate_othername = models.CharField(max_length=50)
    runningmate_surname = models.CharField(max_length=50)
    runningmate_age = models.IntegerField()
    runningmate_nationality = models.CharField(max_length=50)
    runningmate_educationalhistory = models.CharField(max_length=200)
    runningmate_additionaldetails = models.TextField(max_length=200)
    dateadded = models.DateTimeField(default=now)


class PoliticalPost(models.Model):
    postID = models.AutoField(primary_key=True)
    electionID = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)


class SenatorialDistrict(models.Model):
    districtID = models.AutoField(primary_key=True)
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)
    districtname = models.CharField(max_length=50)
    composition = models.TextField(max_length=100)

class Ward(models.Model):
    wardID = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

class Ballot(models.Model):
    voteID = models.AutoField(primary_key=True)
    electionID = models.ForeignKey(ElectionType, on_delete=models.CASCADE, null=True)
    candidateID = models.ForeignKey(PoliticalCandidate, on_delete=models.CASCADE)
    # voters = models.ForeignKey(VoterReg, on_delete=models.CASCADE)
    dateadded = models.DateTimeField(auto_now_add=True)
