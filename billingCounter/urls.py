# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, BillViewSet, OrderedProductViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orderedProducts', OrderedProductViewSet)
router.register(r'bill', BillViewSet)
 

urlpatterns = [
    path('', include(router.urls)),
]
