from django.contrib import admin
from trip.models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'initiator', 'start_date']

# Register your models here.
