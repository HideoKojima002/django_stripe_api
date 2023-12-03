from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
import stripe
from .models import Item, Order, Discount, Tax


def index(request):
    all_item = Item.objects.all()
    return render(request, 'index.html', {'all_item': all_item})


def item_view(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item.html', {'item': item})


def buy_view(request, id):
    item = get_object_or_404(Item, id=id)
    order = Order.objects.create()
    order.items.add(item)
    currency = order.get_currency()
    if currency == 'USD':
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
    elif currency == 'RUB':
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
    else:
        raise ValueError('Unsupported currency')
    # Oбъект сессии stripe с параметрами:
    # - payment_method_types: ['card']
    # - line_items: [{'price_data': {'currency': currency, 'product_data': {'name': item.name, 'description': item.description}, 'unit_amount': order.get_total_price_in_cents()}, 'quantity': 1}]
    # - mode: 'payment'
    # - success_url: 'http://localhost:8000/success/'
    # - cancel_url: 'http://localhost:8000/cancel/'
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': order.get_total_price_in_cents()
            },
            'quantity': 1
        }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/'
    )
    return JsonResponse({'session_id': session.id, 'stripe_public_key': stripe_public_key})