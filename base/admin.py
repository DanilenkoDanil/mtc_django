from django.contrib import admin
from .models import Setting, Number, DelNumber, Payment, Log


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'date')


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    pass


@admin.register(DelNumber)
class DelNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    pass
