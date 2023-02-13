from .models import Order

from functools import reduce
import operator
import ipdb


def calculate_quantity(cart):
    orders = Order.objects.filter(cart=cart)
    return reduce(operator.add, (order.quantity for order in orders))
    