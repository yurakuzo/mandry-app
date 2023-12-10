from django import forms
from trip.models import Trip, TripImage


class TripCreationForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'destination', 'description', 'max_passengers', 'start_date']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def save(self, **kwargs):
        user = kwargs.pop('user', None)
        instance = super().save(commit=False)
        if user:
            instance.initiator = user
        instance.save()
        return instance
    

class UpdateTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'destination', 'description', 'max_passengers', 'start_date', 'difficulty']


class TripImageForm(forms.ModelForm):
    class Meta:
        model = TripImage
        fields = ['image']
