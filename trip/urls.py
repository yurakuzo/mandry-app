
from django.urls import path
from trip.views import MyTripsView
from trip.views import TripCreationView
from trip.views import TripDetailView
from trip.views import AllTripsView


urlpatterns = [
    path('mytrips/', MyTripsView.as_view(), name='mytrips'),
    path("create-trip/", TripCreationView.as_view(), name="create_trip"),
    path('<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
    path('all-trips/', AllTripsView.as_view(), name='all_trips'),

]
