from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Traveller(AbstractUser):
    first_name = models.CharField('first_name', max_length=35)
    last_name = models.CharField('first_name', max_length=35)
    phone_number = models.CharField(
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(12)
        ]
    )
    email = models.EmailField(db_index=True, unique=True)
    image = models.FileField(upload_to='profile_images/', default='profile_images/default-image.jpg')
    rating = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"Traveller({self.email})"


class Comment(models.Model):
    author = models.ForeignKey(Traveller, on_delete=models.CASCADE, related_name='comment_author')
    receiver = models.ForeignKey(Traveller, on_delete=models.CASCADE, related_name='comment_receiver')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment({self.receiver}:{self.author})"
