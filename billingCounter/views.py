from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import Product, Bill, Order
from .serializers import UserSerializer, ProductSerializer, BillSerializer, OrderSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset= Bill.objects.all()
    serializer_class = BillSerializer
    def create(self, request):
        employee = request.data.get('employee')
        customer = request.data.get('customer')
        products_data = request.data.get('products', [])

        bill = Bill.objects.create(employee=employee, customer=customer)
        try:
            for product_data in products_data:
                product = Product.objects.get(pk=product_data.id)
                if product.quantity < product_data.quantity:
                    return Response({'error': 'Insufficient quantity available'}, status=status.HTTP_400_BAD_REQUEST)
                product.quantity -= product_data.quantity
                product.save()
                price = product.price * product_data.quantity
                order = Order.objects.create(bill=bill, product=product, quantity=product_data.quantity, price=price)
            
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

        total = sum(Order.objects.filter(bill=bill).price)
        bill.total = total
        bill.save()

        bill_serializer = BillSerializer(bill)
        return Response(bill_serializer.data, status=status.HTTP_201_CREATED)
