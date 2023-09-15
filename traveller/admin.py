from django.contrib import admin
from traveller.models import Traveller, Comment


@admin.register(Traveller)
class TravellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'rating']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'receiver', 'created_at']
