from django.urls import path
from trip.views import TripCreationView

urlpatterns = [
    path("create-trip/", TripCreationView.as_view(), name="create_trip")
]
