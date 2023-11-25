
from django.urls import path
from trip.views import MyTripsView
from trip.views import TripCreationView
from trip.views import TripDetailView

urlpatterns = [
    path('mytrips/', MyTripsView.as_view(), name='mytrips'),
    path("create-trip/", TripCreationView.as_view(), name="create_trip"),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip_detail')
]
