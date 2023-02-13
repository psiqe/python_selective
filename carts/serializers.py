from rest_framework import serializers

from orders.serializers import OrderSerializer
from orders.models import Order

from .models import Cart
import ipdb

class CartSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = "__all__"
    
    def get_orders(self, instance):
        orders = Order.objects.filter(active=True)
        return OrderSerializer(orders, many=True).data
