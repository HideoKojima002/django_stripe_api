from django.urls import path, include

from .views import item_view, buy_view, index

urlpatterns = [
    path('', index),
    path('item/<int:id>/', item_view, name='item'),
    path('buy/<int:id>/', buy_view, name='buy'),
]
