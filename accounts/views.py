from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .permissions import IsAccountOwner, IsAuthenticatedToGet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import ipdb
from rest_framework.views import APIView, Response, Request, status


class UserView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedToGet]

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
