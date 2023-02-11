from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GamesSerializer
import json

@api_view(['POST'])
def load_games(request):
    games_data = json.loads(request.body)
    for game_data in games_data:
        serializer = GamesSerializer(data=game_data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
    return Response({'message': 'Games apply with success'})
