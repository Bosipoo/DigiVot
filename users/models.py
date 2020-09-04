from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from digivotapp.models import State, Region
from uuid import uuid4


class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_voter = models.BooleanField(default=False)
    created_by = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    profile_completed = models.BooleanField(default=False)

    # The stupid way - I should use one function
    def get_admin_id(self):
        try:
            return Profile.objects.get(user=self).admin_id
        except Profile.DoesNotExist:
            return ''

    def get_phone(self):
        try:
            return Profile.objects.get(user=self).phone_number
        except Profile.DoesNotExist:
            return ''

    def get_gender(self):
        try:
            return Profile.objects.get(user=self).gender
        except Profile.DoesNotExist:
            return ''

    def get_date_of_birth(self):
        try:
            return Profile.objects.get(user=self).date_of_birth
        except Profile.DoesNotExist:
            return ''


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:"
                                         "'+234**********'. 14 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=14)
    date_of_birth = models.DateField(null=True, blank=True)
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
    ),default='')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    region = models.CharField(max_length=50, default='')
    nationality = models.CharField(max_length=50, default='')
    religion = models.CharField(max_length=50, default='')
    profession = models.CharField(max_length=50, default='')
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    address = models.CharField(max_length=200, default='')
    admin_id = models.UUIDField(default=uuid4)


class AuthenticationTable(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)
    key = models.CharField(max_length=50)
