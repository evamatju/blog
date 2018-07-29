#coding=utf-8
from django.db import models

# Create your models here.

class Article(models.Model):
    username = models.CharField(max_length=30,unique=True)
    # gender = models.CharField('级别', choices=(('M', '男'), ('F', '女')),
    #                           maxlength=1, radio_admin=True)
    level = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)

class Order(models.Model):
    orderId = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=30,unique=True)
    # gender = models.CharField('级别', choices=(('M', '男'), ('F', '女')),
    #                           maxlength=1, radio_admin=True)
    detail = models.CharField(max_length=3000)
    type = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    publisher = models.CharField(max_length=30)
    operator = models.CharField(max_length=30)
    progress = models.IntegerField(default=0)


class Device(models.Model):
    deviceId = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=30,unique=True)
    # gender = models.CharField('级别', choices=(('M', '男'), ('F', '女')),
    #                           maxlength=1, radio_admin=True)
    detail = models.CharField(max_length=3000)
    type = models.CharField(max_length=30)
