from django.shortcuts import render
from django.views import generic
from trip.models import Trip, Comment, TripImage
from django.urls import reverse_lazy
from trip.forms import TripCreationForm, TripImageForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class MyTripsView(ListView):
    model = Trip
    template_name = 'trip/my_trip.html'
    context_object_name = 'user_trips'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Trip.objects.filter(initiator=self.request.user)
        else:
            return Trip.objects.none()


class TripCreationView(LoginRequiredMixin, generic.CreateView):
    form_class = TripCreationForm
    success_url = reverse_lazy('mytrips')
    template_name = 'trip/create_trip.html'
    model = Trip

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(TripCreationView, self).form_valid(form)

    def form_invalid(self, form):
        return super(TripCreationView, self).form_invalid(form)


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


class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Trip
    form_class = TripCreationForm
    template_name = 'trip/edit_trip.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['images'] = TripImageForm(self.request.POST, self.request.FILES)
        else:
            data['images'] = TripImageForm()
        return data

    def form_valid(self, form):
        self.object = form.save()
        for img_file in self.request.FILES.getlist('image'):
            TripImage.objects.create(trip=self.object, image=img_file)
        return super().form_valid(form)

    def test_func(self):
        trip = self.get_object()
        return self.request.user == trip.initiator


def trip_details(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)

    if request.method == 'POST' and request.user.is_authenticated:
        comment_text = request.POST.get('comment')
        Comment.objects.create(trip=trip, user=request.user, text=comment_text)
        return redirect('trip_details', trip_id=trip_id)

    return render(request, 'trip_details.html', {'trip': trip})
