from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.timezone import now
import datetime
import string


# Create your models here.
class Super_Registeradmin(models.Model):
    pin = models.CharField(primary_key=True, default ="A" + get_random_string(4, allowed_chars=string.ascii_uppercase + string.digits), max_length=5, editable=False)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    

class AdminUserR(models.Model):
    adminID = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    othername = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+234**********'. 14 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=14) # validators should be a list
    email = models.EmailField(max_length=100)
    DOB = models.DateField()
    address = models.TextField(max_length=200)
    gender = models.CharField(max_length=50, choices=(
        ('male','Male'), 
        ('female','Female')
    ), default='Female')
    status = models.CharField(max_length=50, choices=(
        ('married','Married'),
        ('unmarried','Unmarried')
    ), default='status')
    List_of_states= [
        ('abia','Abia'),
        ('adamawa','Adamawa'),
        ('akwa ibom','Akwa Ibom'),
        ('anambra','Anambra'),
        ('bauchi','Bauchi'),
        ('bayelsa','Bayelsa'),
        ('benue','Benue'),
        ('borno','Borno'),
        ('cross river','Cross River'),
        ('delta','Delta'),
        ('ebonyi','Ebonyi'),
        ('edo','Edo'),
        ('ekiti','Ekiti'),
        ('enugu','Enugu'),
        ('gombe','Gombe'),
        ('imo','Imo'),
        ('jigawa','Jigawa'),
        ('kaduna','Kaduna'),
        ('kano','Kano'),
        ('katsina','Katsina'),
        ('kebbi','Kebbi'),
        ('kogi','Kogi'),
        ('kwara','Kwara'),
        ('lagos','Lagos'),
        ('nasarawa','Nasarawa'),
        ('niger','Niger'),
        ('ogun','Ogun'),
        ('ondo','Ondo'),
        ('osun','Osun'),
        ('oyo','Oyo'),
        ('plateau','Plateau'),
        ('rivers','Rivers'),
        ('sokoto','Sokoto'),
        ('taraba','Taraba'),
        ('yobe','Yobe'),
        ('zamfara','Zamfara'),
        ('fct','FCT'),
    ]
    states = models.CharField(max_length=50, choices=List_of_states)
    region = models.CharField(max_length=50, default='surulere')
    pictures = models.ImageField(upload_to='Images/')
    finger1 = models.BinaryField()
    finger2 = models.BinaryField()
    
class AdminUserLogin(models.Model):
    adminID = models.ForeignKey(AdminUserR, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class ManagerUserR(models.Model):
    managerID = models.AutoField(primary_key=True)
    # adminID = models.ForeignKey(AdminUserR, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    othername = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+234**********'. 14 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=14) # validators should be a list
    email = models.EmailField(max_length=100)
    DOB = models.DateField()
    gender = models.CharField(max_length=50, choices=(
        ('male','Male'), 
        ('female','Female')
    ), default='Female')
    address = models.TextField(max_length=200)
    pictures = models.ImageField(upload_to='Images/')
    # finger1 = models.BinaryField()
    # finger2 = models.BinaryField()
    pin = models.CharField(default ="M" + get_random_string(4, allowed_chars=string.ascii_uppercase + string.digits), max_length=5, editable=False)
    dateadded = models.DateTimeField(default=now)


class ManagerUserLogin(models.Model):
    managerID = models.ForeignKey(ManagerUserR, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class VoterReg(models.Model):
    voterID = models.AutoField(primary_key=True)
    #managerID = models.ForeignKey(ManagerUserR, on_delete=models.CASCADE)

    firstname = models.CharField(max_length=20)
    othername = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+234**********'. 14 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=14) # validators should be a list
    email = models.EmailField(max_length=100)
    DOB = models.DateField()
    status = models.CharField(max_length=50, choices=(
        ('married','Married'),
        ('unmarried','Unmarried')
    ), default='status')
    title = models.CharField(max_length=50, choices=(
        ('mr','Mr'), 
        ('ms','Ms'),
        ('mrs','Mrs')
    ))
    List_of_states= [
        ('abia','Abia'),
        ('adamawa','Adamawa'),
        ('akwa ibom','Akwa Ibom'),
        ('anambra','Anambra'),
        ('bauchi','Bauchi'),
        ('bayelsa','Bayelsa'),
        ('benue','Benue'),
        ('borno','Borno'),
        ('cross river','Cross River'),
        ('delta','Delta'),
        ('ebonyi','Ebonyi'),
        ('edo','Edo'),
        ('ekiti','Ekiti'),
        ('enugu','Enugu'),
        ('gombe','Gombe'),
        ('imo','Imo'),
        ('jigawa','Jigawa'),
        ('kaduna','Kaduna'),
        ('kano','Kano'),
        ('katsina','Katsina'),
        ('kebbi','Kebbi'),
        ('kogi','Kogi'),
        ('kwara','Kwara'),
        ('lagos','Lagos'),
        ('nasarawa','Nasarawa'),
        ('niger','Niger'),
        ('ogun','Ogun'),
        ('ondo','Ondo'),
        ('osun','Osun'),
        ('oyo','Oyo'),
        ('plateau','Plateau'),
        ('rivers','Rivers'),
        ('sokoto','Sokoto'),
        ('taraba','Taraba'),
        ('yobe','Yobe'),
        ('zamfara','Zamfara'),
        ('fct','FCT'),
    ]
    statesoforigin = models.CharField(max_length=50, choices=List_of_states)
    regionoforigin = models.CharField(max_length=50, default='surulere')
    statesofresidence = models.CharField(max_length=50, choices=List_of_states)
    regionofresidence = models.CharField(max_length=50, default='surulere')
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    pictures = models.ImageField(upload_to='Images/')
    finger1 = models.BinaryField()
    finger2 = models.BinaryField()
    pin = models.CharField(default = "V" + get_random_string(4, allowed_chars=string.ascii_uppercase + string.digits), max_length=5, editable=False)
    dateadded = models.DateTimeField(default=now)


    def __int__(self):
        return self.voterID

class PoliticalParty(models.Model):
    partyID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=10)
    symbol = models.ImageField(upload_to='Images/')

class ElectionType(models.Model):
    electionID = models.AutoField(primary_key=True)
    electiontype = models.CharField(max_length=100) 
    registeration_start = models.DateField()
    registeration_end = models.DateField()
    voting_start = models.DateField()
    voting_end = models.DateField()
    requiredposition = models.TextField(max_length=200)
    dateadded = models.DateTimeField(default=now)

class PoliticalCandidate(models.Model):
    candidateID = models.AutoField(primary_key=True)
    partyID = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE)
    electionID = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    candidate_firstname = models.CharField(max_length=50)
    candidate_othername = models.CharField(max_length=50)
    candidate_surname = models.CharField(max_length=50)
    candidate_details = models.TextField(max_length=200)
    running_firstname = models.CharField(max_length=50)
    running_othername = models.CharField(max_length=50)
    runningmate_surname = models.CharField(max_length=50)
    runningmate_details = models.TextField(max_length=200)
    dateadded = models.DateTimeField(default=now)

class PoliticalPost(models.Model):
    postID = models.AutoField(primary_key=True)
    electionID = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

class State(models.Model):
    stateID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class LGA(models.Model):
    lgaID = models.AutoField(primary_key=True)
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

class  SenatorialDistrict(models.Model):
    districtID = models.AutoField(primary_key=True)
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)
    districtname = models.CharField(max_length=50)
    composition = models.TextField(max_length=100)

class Ward(models.Model):
    wardID = models.AutoField(primary_key=True)
    lgaID = models.ForeignKey(LGA, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Ballot(models.Model):
    voteID = models.AutoField(primary_key=True)
    candidateID = models.ForeignKey(PoliticalCandidate, on_delete=models.CASCADE)
    voters = models.ForeignKey(VoterReg, on_delete=models.CASCADE)
    dateadded = models.DateTimeField(auto_now_add=True)

