from django.shortcuts import render
from django.views import generic
from trip.models import Trip, Comment
from django.urls import reverse_lazy
from trip.forms import TripCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect


class MyTripsView(ListView):
    model = Trip
    template_name = 'trip/my_trip.html'
    context_object_name = 'user_trips'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Trip.objects.filter(initiator=self.request.user)
        else:
            return Trip.objects.none()


class TripCreationView(generic.CreateView):
    form_class = TripCreationForm
    success_url = reverse_lazy('main_page')
    template_name = 'trip/create_trip.html'
    model = Trip

    def form_valid(self, form):
        # Set the initiator to the user making the request
        form.instance.initiator = self.request.user
        # Call the super class form_valid to save the form and redirect to success_url
        return super(TripCreationView, self).form_valid(form)


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip/trip_detail.html'

    def post(self, request, *args, **kwargs):
        trip = self.get_object()
        if 'join' in request.POST:
            trip.join_trip(request.user)
            return redirect("trip_detail", pk=trip.pk)
        elif 'leave' in request.POST:
            trip.leave_trip(request.user)
            return redirect("trip_detail", pk=trip.pk)
        elif 'comment' in request.POST and request.user.is_authenticated:
            comment_text = request.POST.get('comment')
            Comment.objects.create(trip=trip, user=request.user, text=comment_text)
            return redirect("trip_detail", pk=trip.pk)
        return render(request, self.template_name, {'trip': trip})


class AllTripsView(ListView):
    model = Trip
    template_name = 'trip/trip.html'
    context_object_name = 'all_trips'


def trip_details(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)

    if request.method == 'POST' and request.user.is_authenticated:
        comment_text = request.POST.get('comment')
        Comment.objects.create(trip=trip, user=request.user, text=comment_text)
        return redirect('trip_details', trip_id=trip_id)
    return render(request, 'trip_details.html', {'trip': trip})
