from rest_framework import serializers

from django.shortcuts import get_object_or_404

from carts.models import Cart
from .models import Order
from .utils import calculate_quantity

from decimal import Decimal
import ipdb


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cart = serializers.HiddenField(default=None)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ["cart", "user"]


    def create(self, validated_data):
        if validated_data['quantity'] < 1:
            raise serializers.ValidationError("The amount value must be an integer greater than 0")
        
        user = self.context['request'].user
        # método get_or_create retorna objeto e booleano respectivamente
        cart, created = Cart.objects.get_or_create(user=user, active=True)

        order = Order.objects.filter(product=validated_data['product']).first()
        
        if(order):
            order.quantity += validated_data['quantity']
            order.shipping += 10 * validated_data['quantity']
            order.subtotal += Decimal(validated_data['product'].price * validated_data['quantity'])
            order.save()
        else:
            order = Order(**validated_data)
            order.shipping = 10 * validated_data['quantity']
            order.subtotal = Decimal(validated_data['product'].price * validated_data['quantity'])
            
        
        cart.subtotal += Decimal(validated_data['product'].price * validated_data['quantity'])
    
        if cart.subtotal >= 250:
            cart.shipping = 0
        else: 
            cart.shipping += 10 * validated_data['quantity']   
        cart.total = cart.subtotal + cart.shipping
        
        cart.save()

        order.cart = cart    
        order.save()    

        return order
    
    def update(self, instance, validated_data):
        if validated_data['quantity'] < 1:
            raise serializers.ValidationError("If you want to reset the order, you will need to delete it.")
        user = self.context['request'].user
        cart, created = Cart.objects.get_or_create(user=user, active=True)

        if instance.subtotal > (Decimal(instance.product.price * validated_data['quantity'])):
            cart.subtotal -= (instance.subtotal - (Decimal(instance.product.price * validated_data['quantity'])))
        elif instance.subtotal < Decimal(instance.product.price * validated_data['quantity']):
            cart.subtotal += ((Decimal(instance.product.price * validated_data['quantity'])) - instance.subtotal)
        

        instance.quantity = validated_data['quantity']
        instance.shipping = 10 * validated_data['quantity']
        instance.subtotal = Decimal(instance.product.price * validated_data['quantity'])
        instance.save()
        
        if cart.subtotal >= 250:
            cart.shipping = 0
        else:
            cart.shipping = calculate_quantity(cart) * 10
        cart.total = cart.subtotal + cart.shipping
        cart.save()

        return instance
