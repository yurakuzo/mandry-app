from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from mandry.views import MainPageView
from trip.views import MytTripsView

urlpatterns = [
    path('mytrips/', MytTripsView.as_view(), name='mytrips')
]
