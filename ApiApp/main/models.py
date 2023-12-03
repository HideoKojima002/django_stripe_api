from django.db import models
from django.conf import settings
import stripe


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('USD', 'US Dollar'), ('RUB', 'Rub')])

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'Order #{self.id}'

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total

    def get_total_price_in_cents(self):
        return int(self.get_total_price() * 100)

    def get_currency(self):
        currency = None
        for item in self.items.all():
            if currency is None:
                currency = item.currency
            elif currency != item.currency:
                raise ValueError('Order items must have the same currency')
        return currency


class Discount(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name