from django import forms  # noqa: disable=f401
from django.contrib.auth.forms import UserCreationForm
from .models import Traveller


class SignUpForm(UserCreationForm):
    class Meta:
        model = Traveller
        fields = ['email', 'username', 'password1', 'password2']
