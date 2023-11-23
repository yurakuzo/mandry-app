
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from mandry.views import MainPageView
from trip.views import MyTripsView
from django.urls import path
from trip.views import TripCreationView
urlpatterns = [
    path('mytrips/', MyTripsView.as_view(), name='mytrips'),
    path("create-trip/", TripCreationView.as_view(), name="create_trip")
]