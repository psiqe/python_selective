from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from .filters import GamesFilter
from .models import Games
from .serializers import GamesSerializer

class GamesList(generics.ListAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = GamesFilter
    ordering_fields = ['price', 'score', 'name']