# urls.py
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, BillViewSet, OrderedProductViewSet, LogoutView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orderedProducts', OrderedProductViewSet)
router.register(r'bill', BillViewSet)
 

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('logout/', LogoutView.as_view(), name ='logout'),
    path('', include(router.urls)),
]
