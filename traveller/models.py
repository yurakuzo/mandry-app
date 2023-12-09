from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

class Traveller(AbstractUser):
    first_name = models.CharField('first_name', max_length=35)
    last_name = models.CharField('last_name', max_length=35)
    phone_number = models.CharField(
        max_length=12,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(12)
        ]
    )
    email = models.EmailField(db_index=True, unique=True)
    image = models.FileField(upload_to='profile_images/', default='profile_images/default-image.jpg')

    @property
    def user_comments(self):
        return self.comment_receiver.all()

    @property
    def user_rating(self):
        average_rating = self.comment_receiver.aggregate(avg_rating=Avg('rating'))['avg_rating']
        return average_rating or 0

    def __str__(self) -> str:
        return f"Traveller({self.email})"

class Comment(models.Model):
    author = models.ForeignKey(Traveller, on_delete=models.CASCADE, related_name='comment_author')
    receiver = models.ForeignKey(Traveller, on_delete=models.CASCADE, related_name='comment_receiver')
    comment = models.TextField(blank=False, null=False, default='Comment example')
    rating = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment({self.receiver}:{self.author})"
