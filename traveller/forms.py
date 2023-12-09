from django import forms  # noqa: disable=f401
from django.contrib.auth.forms import UserCreationForm
from .models import Traveller
from .models import Comment


class SignUpForm(UserCreationForm):
    class Meta:
        model = Traveller
        fields = ['email', 'username', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Traveller
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'rating']
