from django import forms
from trip.models import Trip


class TripCreationForm(forms.ModelForm):
    # start_date = forms.DateTimeField(widget=forms.DateTimeInput)
    class Meta:
        model = Trip
        fields = ['title', 'destination', 'description', 'max_passangers', 'start_date']
        widgets = {
            'start_date': forms.DateTimeField
        }
        
    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(TripCreationForm, self).save(**kwargs)
        instance.user = user
        instance.save()
        return instance

