from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Product, Order, Bill

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password' : {'write_only': True}}

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ['product', 'quantity', 'price']

class BillSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ('id', 'billNumber', 'employee', 'customer', 'total', 'orders')

    def create(self, validated_data):
        orders_data = validated_data.pop('orders', [])
        bill = Bill.objects.create(**validated_data)

        for order_data in orders_data:
            Order.objects.create(bill=bill, **order_data)

        return bill
