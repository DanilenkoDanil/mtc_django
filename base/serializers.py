from rest_framework import serializers
from .models import Number, Setting, Payment, Log, DelNumber
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"


class NumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Number
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Setting
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = "__all__"


class DelNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = DelNumber
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
