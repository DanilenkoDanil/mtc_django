from rest_framework import viewsets, status, generics, permissions, views
from .serializers import NumberSerializer, SettingSerializer, LogSerializer, DelNumberSerializer, PaymentSerializer
from .models import Number, Setting, Log, DelNumber, Payment


class NumberViewSet(viewsets.ModelViewSet):
    serializer_class = NumberSerializer
    queryset = Number.objects.all()


class SettingViewSet(viewsets.ModelViewSet):
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()


class LogAPIView(generics.ListAPIView):
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class DelNumberAPIView(generics.ListAPIView):
    serializer_class = DelNumberSerializer
    queryset = DelNumber.objects.all()


class PaymentAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


