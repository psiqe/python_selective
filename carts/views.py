from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CartSerializer
from .models import Cart

from django.shortcuts import get_object_or_404


class CartView(APIView):
    queryset = Cart
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        
        return Response(serializer.data)

class CartDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        cart = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(cart)
        
        return Response(serializer.data)
