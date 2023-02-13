from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Response, Request, status
from rest_framework.response import Response

from .permissions import IsAuthenticatedToGet
from .serializers import UserSerializer
from .models import User

from django.shortcuts import get_object_or_404
import ipdb


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedToGet]
    serializer_class = UserSerializer
    queryset = User

    def get(self, request: Request) -> Response:
        user = get_object_or_404(User, id=request._auth.payload['user_id'])
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


    def patch(self, request: Request) -> Response:
        user = get_object_or_404(User, id=request._auth.payload['user_id'])
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request) -> Response:
        user = get_object_or_404(User, id=request._auth.payload['user_id'])
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
