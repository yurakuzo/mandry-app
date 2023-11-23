from django.db import models
from traveller.models import Traveller


class Trip(models.Model):
    title = models.CharField(max_length=35, default="Trip")
    destination = models.CharField(max_length=70, default="Destination")
    description = models.TextField()
    initiator = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    max_passangers = models.IntegerField(default=5)
    passangers = models.ManyToManyField('traveller.Traveller', blank=True, related_name='trip_passangers')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=False, null=False)

    def __str__(self) -> str:
        return f"Trip({self.initiator};{len(self.passangers.all())})"
