from rest_framework import serializers
from medicines.models import Medicine
from .models import Order


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'title', 'category', 'image', 'manufactured_by', 'price', 'stock']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['medicine', 'quantity']
