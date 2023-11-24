
from django.urls import path
from trip.views import MyTripsView
from trip.views import TripCreationView
urlpatterns = [
    path('mytrips/', MyTripsView.as_view(), name='mytrips'),
    path("create-trip/", TripCreationView.as_view(), name="create_trip")
]
