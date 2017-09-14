from django.db import models
from goods.models import GoodsInfo
from user.models import UserInfo

# Create your models here.


""" 不合适的模型
class CartsGoods(models.Model):
    ctitle = models.CharField(max_length=50)
    cpic = models.ImageField(upload_to='goods/')
    cprice = models.DecimalField(max_digits=5,decimal_places=2)
    cunit = models.CharField(max_length=20)
    cisdelte = models.BooleanField(default=False)
    ctotal = models.IntegerField()
"""

class CartsGoods(models.Model):
    c_count = models.IntegerField()
    cgoods = models.ForeignKey(GoodsInfo)
    cuser = models.ForeignKey(UserInfo)
