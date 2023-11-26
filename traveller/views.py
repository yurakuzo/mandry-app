from django.shortcuts import render, redirect  # noqa: disable=f401
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .forms import SignUpForm
from django.contrib.auth import login

from traveller.models import Traveller


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    template_name = 'traveller/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'traveller/profile.html'


class ProfileDetailView(DetailView):
    model = Traveller
    template_name = 'traveller/profile.html'
    context_object_name = 'user'
