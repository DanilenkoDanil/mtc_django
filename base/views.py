from rest_framework import viewsets, status, generics, permissions, views
from .serializers import NumberSerializer, SettingSerializer, LogSerializer, DelNumberSerializer, PaymentSerializer
from .models import Number, Setting, Log, DelNumber, Payment
from rest_framework.response import Response


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


class GetCodeAPIView(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        number = request.query_params.get('number')
        if number is None:
            return Response(f"Не указан номер", status=status.HTTP_400_BAD_REQUEST)
        return Response(f"Ваш запрос на номер {number} принят", status=status.HTTP_201_CREATED)


class SendCodeAPIView(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if code is None:
            return Response(f"Не указан код", status=status.HTTP_400_BAD_REQUEST)
        return Response(f"Код принят", status=status.HTTP_201_CREATED)


class ChangeCommentAPIView(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        comment = request.query_params.get('comment')
        number = request.query_params.get('number')

        if number is None:
            return Response(f"Не указан номер", status=status.HTTP_400_BAD_REQUEST)
        if comment is None:
            return Response(f"Не указан комментарий", status=status.HTTP_400_BAD_REQUEST)
        try:
            del_number = DelNumber.objects.get(number=int(number))
            del_number.comment = comment
            del_number.save()
        except DelNumber.DoesNotExist:
            return Response(f"Такой номер не найден в удалённых", status=status.HTTP_400_BAD_REQUEST)

        return Response(f"Коментарий принят", status=status.HTTP_201_CREATED)
