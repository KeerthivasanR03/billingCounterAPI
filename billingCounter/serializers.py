from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Product, OrderedProduct, Bill

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password' : {'write_only': True}}

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = ['product', 'quantity', 'price']

class BillSerializer(serializers.ModelSerializer):
    orderedProducts = OrderedProductSerializer(many=True, source='orderedproduct_set')

    class Meta:
        model = Bill
        fields = ['id', 'billNumber', 'employee', 'customer', 'total', 'orderedProducts']
        read_only_fields = ['total']

    def create(self, validated_data):
        product_list = validated_data.pop('orderedproduct_set', [])
        bill = Bill.objects.create(**validated_data)
        total = 0
        for singleProduct in product_list:
            orderedProductInstance = OrderedProduct.objects.create(bill=bill, product=singleProduct.get('product'), quantity=singleProduct.get('quantity'), price=singleProduct.get('quantity') * singleProduct.get('product').price)
            total += singleProduct.get('quantity') * singleProduct.get('product').price 
        bill.total = total
        bill.save()
        return bill

    
