from django.db import models


class Number(models.Model):
    number = models.IntegerField(unique=True)
    password = models.CharField(max_length=200)
    forwarding = models.IntegerField(blank=True, null=True)
    balance = models.FloatField()
    max_balance = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class DelNumber(models.Model):
    number = models.IntegerField(unique=True)
    password = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    date_create = models.DateTimeField()
    date_del = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Payment(models.Model):
    number = models.IntegerField()
    balance = models.FloatField()
    payment_value = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Log(models.Model):
    task = models.TextField()
    status = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Setting(models.Model):
    time_check = models.IntegerField()
    min_balance = models.FloatField()
    poplni_login = models.CharField(max_length=200)
    poplni_password = models.CharField(max_length=200)
    captcha_guru = models.CharField(max_length=300)
