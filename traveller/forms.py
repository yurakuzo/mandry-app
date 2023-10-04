from django import forms  # noqa: disable=f401
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Traveller


class SignUpForm(UserCreationForm):
    class Meta:
        model = Traveller
        fields = ['email', 'username', 'password1', 'password2']


class UpdateTravellerForm(UserChangeForm):
    class Meta:
        model = Traveller
        fields = ['first_name', 'last_name', 'phone_number', 'image']
