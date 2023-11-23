# api/urls.py
from django.urls import path, include
from .views import TravellerViewSet, CommentViewSet, TripViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'travellers', TravellerViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('', include(router.urls), name='api'),
]
