from django.shortcuts import render # noqa:disable=f401
from django.views import View
from trip.models import Trip

# Create your views here.
class MytTripsView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        print(request.user)
        print(Trip.objects)
        print(Trip.objects.all())
        print(Trip.objects.filter(initiator=request.user))
        if request.user.is_authenticated:
            user_trips = Trip.objects.filter(initiator=request.user)
        else:
            user_trips = Trip.objects.none()  # Or handle as you see fit
        return render(request, self.template_name)

    