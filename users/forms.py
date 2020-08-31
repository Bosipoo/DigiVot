from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'username']


class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user', 'admin_id']
        widgets = {
            'date_of_birth': DateInput()
        }
