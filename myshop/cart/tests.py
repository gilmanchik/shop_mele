from decimal import Decimal

from django.test import TestCase


class Cart:
    def __init__(self):
        self.cart = {1: 'a', 2: 'b'}

    def __iter__(self):
        for i in self.cart.values():
            yield i


cart = Cart()
for i in cart:
    print(i)
