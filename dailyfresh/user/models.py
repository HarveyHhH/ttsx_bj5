# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    umail = models.CharField(max_length=50)
    uaddress = models.CharField(max_length=100, default='')
    uphone = models.CharField(max_length=11, default='')
    urecv = models.CharField(max_length=20, default='')
    ucode = models.CharField(max_length=6,default='')



