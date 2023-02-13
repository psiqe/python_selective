from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from django_filters import rest_framework as filters

from .serializers import GamesSerializer
from .filters import GamesFilter
from .models import Games
import json

class GamesList(generics.ListAPIView):
    queryset = Games
    serializer_class = GamesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = GamesFilter
    ordering_fields = ['price', 'score', 'name']


class LoadGamesView(APIView):
    def post(self, request):
        games_data = json.loads(request.body)
        listResponse = []
        for game_data in games_data:
            serializer = GamesSerializer(data=game_data)
            if serializer.is_valid():
                serializer.save()
                listResponse.append(serializer.data)
            else:
                return Response(serializer.errors, status=400)
        return Response({
            'message': 'Games registered with success',
            'data': listResponse    
        })
