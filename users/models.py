from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from digivotapp.models import State, Region, District
from uuid import uuid4


class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_voter = models.BooleanField(default=False)
    created_by = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:"
                                         "'+234**********'. 14 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=14)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female')
    ), default='')
    marital_status = models.CharField(max_length=10, choices=(
        ('married', 'Married'),
        ('unmarried', 'Unmarried')
    ), default='', blank=True)
    title = models.CharField(max_length=5, choices=(
        ('mr', 'Mr'),
        ('ms', 'Ms'),
        ('mrs', 'Mrs')
    ))
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    address = models.CharField(max_length=200)
    admin_id = models.UUIDField(default=uuid4().hex, null=True)


class AuthenticationTable(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)
    key = models.UUIDField()
