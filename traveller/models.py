from django.db import models
from django.contrib.auth.models import AbstractUser


class Traveller(AbstractUser):
    first_name = models.CharField()
    last_name = models.CharField()
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    rating = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"Traveller({self.email})"

class Comment(models.Model):
    author = models.ForeignKey(Traveller, on_delete=models.CASCADE, related_name='comment_author')
    receiver = models.ForeignKey(Traveller, on_delete=models.CASCADE, related_name='comment_receiver')
    created_at = models.DateTimeField(auto_now_add=True)
