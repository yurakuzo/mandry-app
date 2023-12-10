from django.db import models
from traveller.models import Traveller
from django.urls import reverse

DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('middle', 'Middle'),
        ('hard', 'Hard'),
    ]


class Trip(models.Model):
    title = models.CharField(max_length=35, default="Trip")
    destination = models.CharField(max_length=70, default="Destination")
    description = models.TextField()
    initiator = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    max_passengers = models.IntegerField(default=5)
    passengers = models.ManyToManyField(Traveller, related_name='joined_trips', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=False, null=False)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES, default='easy')

    def __str__(self) -> str:
        return f"Trip({self.initiator};{len(self.passengers.all())})"

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super(Trip, self).save(*args, **kwargs)
        if is_new and self.initiator:
            self.passengers.add(self.initiator)

    def join_trip(self, user):
        self.passengers.add(user)

    def leave_trip(self, user):
        self.passengers.remove(user)

    def get_absolute_url(self):
        return reverse('trip_detail', kwargs={'pk': self.pk})


class TripImage(models.Model):
    trip = models.ForeignKey(Trip, related_name='images', on_delete=models.CASCADE)
    image = models.FileField(upload_to='trip_images/')

    def __str__(self):
        return f"Image for {self.trip.title}"


class Comment(models.Model):
    trip = models.ForeignKey(Trip, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
