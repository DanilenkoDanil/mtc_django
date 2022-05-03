from rest_framework import viewsets, status, generics, permissions, views
from .serializers import NumberSerializer, SettingSerializer, LogSerializer, DelNumberSerializer, \
    PaymentSerializer, UserSerializer, PermissionSerializer
from .models import Number, Setting, Log, DelNumber, Payment
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


class NumberViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = NumberSerializer
    queryset = Number.objects.all()


class SettingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = SettingSerializer
    queryset = Setting.objects.all()


class LogAPIView(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class DelNumberAPIView(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = DelNumberSerializer
    queryset = DelNumber.objects.all()


class PermissionAPIView(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


class PaymentAPIView(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class GetCodeAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        number = request.query_params.get('number')
        if number is None:
            return Response(f"Не указан номер", status=status.HTTP_400_BAD_REQUEST)
        return Response(f"Ваш запрос на номер {number} принят", status=status.HTTP_201_CREATED)


class SendCodeAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if code is None:
            return Response(f"Не указан код", status=status.HTTP_400_BAD_REQUEST)
        return Response(f"Код принят", status=status.HTTP_201_CREATED)


class ChangeCommentAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]

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


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()


class CheckAccountAPIView(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        login = request.data.get('login')
        password = request.data.get('password')
        if login is None or password is None:
            return Response(f"Параметры login, password обязательны", status=status.HTTP_404_NOT_FOUND)
        try:
            user = User.objects.get(username=login)
            if not user.check_password(password):
                return Response(f"Не подходит логин или пароль", status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response(f"Не подходит логин или пароль", status=status.HTTP_404_NOT_FOUND)

        return Response(f"Логин и пароль верны", status=status.HTTP_200_OK)
