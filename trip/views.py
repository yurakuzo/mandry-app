from django.shortcuts import render # noqa:disable=f401
from django.views import generic
from trip.models import Trip
from django.urls import reverse_lazy
from trip.forms import TripCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Trip

def search_trips(request):
    query = request.GET.get('q', '')
    if query:
        trips = Trip.objects.filter(
            Q(title__icontains=query) |
            Q(destination__icontains=query) |
            Q(initiator__username__icontains=query)
        ).values('id', 'title', 'destination')  # Adjust fields as needed
        return JsonResponse(list(trips), safe=False)
    return JsonResponse([])
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
            return redirect("all_trips")
        elif 'leave' in request.POST:
            trip.leave_trip(request.user)
            return redirect("all_trips")
        return render(request, self.template_name, trip)


from django.db.models import Count, Q

class AllTripsView(ListView):
    model = Trip
    template_name = 'trip/trip.html'
    context_object_name = 'all_trips'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort')
        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(initiator__username__icontains=search_query)
            )

        if sort:
            if sort == "travelers_asc":
                queryset = queryset.annotate(num_travelers=Count('passengers')).order_by('num_travelers')
            elif sort == "travelers_desc":
                queryset = queryset.annotate(num_travelers=Count('passengers')).order_by('-num_travelers')
            elif sort in ["title", "-title"]:
                queryset = queryset.order_by(sort)

        return queryset

  
