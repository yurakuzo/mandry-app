from django.contrib import admin
from trip.models import Trip, TripImage


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'destination', 'initiator', 'start_date']


admin.site.register(TripImage)
