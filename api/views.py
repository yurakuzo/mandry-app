# api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from traveller.models import Traveller, Comment
from trip.models import Trip
from .serializers import TravellerSerializer, CommentSerializer, TripSerializer


class TravellerViewSet(viewsets.ModelViewSet):
    queryset = Traveller.objects.all()
    serializer_class = TravellerSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def create(self, request, *args, **kwargs):
        author = request.user
        receiver_id = request.data.get('receiver')

        if Comment.objects.filter(author=author, receiver_id=receiver_id).exists():
            return Response({"detail": "You have already commented on this user."}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer