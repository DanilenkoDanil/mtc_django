from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NumberViewSet, SettingViewSet, PaymentAPIView, LogAPIView, DelNumberAPIView


router = DefaultRouter()
router.register('number', NumberViewSet, basename='number')
router.register('setting', SettingViewSet, basename='setting')

urlpatterns = [
    path('payment/', PaymentAPIView.as_view(), name='payment'),
    path('log/', LogAPIView.as_view(), name='log'),
    path('del/', DelNumberAPIView.as_view(), name='del'),
    path('', include(router.urls))
]
