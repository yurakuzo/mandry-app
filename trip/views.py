from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from trip.forms import TripCreationForm
from trip.models import Trip


class TripCreationView(generic.CreateView):
    form_class = TripCreationForm
    success_url = reverse_lazy('main_page')
    template_name = 'trip/create_trip.html'
    model = Trip

    def form_valid(self, form, request):
        if form.is_valid():
            response = form.save(user=request.user, commit=False)
        # response = super().form_valid(form)
        print(response, response.json())
        return response
