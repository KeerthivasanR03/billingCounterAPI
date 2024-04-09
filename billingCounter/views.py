from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from django.db.models import Sum
from .models import Product, Bill, OrderedProduct
from .serializers import UserSerializer, ProductSerializer, BillSerializer, OrderedProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderedProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OrderedProduct.objects.all()
    serializer_class = OrderedProductSerializer

class BillViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset= Bill.objects.all()
    serializer_class = BillSerializer
    # def create(self, request):
    #     employee = request.data.get('employee')
    #     customer = request.data.get('customer')
    #     products_data = request.data.get('products', [])

    #     employee = User.objects.get(pk=employee)
    #     customer = User.objects.get(pk=customer)
    #     bill = Bill.objects.create(employee=employee, customer=customer)
    #     try:
    #         for product_data in products_data:
    #             quantity = product_data.get('quantity')
    #             product = Product.objects.get(pk=product_data.get('id'))
    #             if product.quantity < quantity:
    #                 return Response({'error': 'Insufficient quantity available'}, status=status.HTTP_400_BAD_REQUEST)
    #             product.quantity -= quantity
    #             product.save()
    #             price = product.price * quantity
    #             order = Order.objects.create(bill=bill, product=product, quantity=quantity, price=price)
            
    #     except Product.DoesNotExist:
    #         return Response({'error': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

    #     total = Order.objects.filter(bill=bill).values('price').aggregate(total_price=Sum('price'))['total_price']
    #     bill.total = total
    #     bill.save()

    #     bill_serializer = BillSerializer(bill)
    #     return Response(bill_serializer.data, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)
