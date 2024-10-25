# orders/urls.py
from django.urls import path
from .views import coffee_list, create_order, receipt_detail

urlpatterns = [
    path('', coffee_list, name='coffee_list'),
    path('create_order/', create_order, name='create_order'),
    path('receipt/<int:receipt_id>/', receipt_detail, name='receipt'),
]