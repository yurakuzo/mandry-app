from django import forms
from trip.models import Trip


class TripCreationForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'destination', 'description', 'max_passengers', 'start_date']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Corrected widget
        }

    def save(self, **kwargs):
        user = kwargs.pop('user', None)
        instance = super().save(commit=False)  # Calling super with commit=False
        if user:
            instance.initiator = user  # Assuming initiator is the field to link to the user
        instance.save()
        return instance
