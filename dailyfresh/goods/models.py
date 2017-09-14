from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    tisdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=50)
    gpic = models.ImageField(upload_to='goods/')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    gclick = models.IntegerField()
    gunit = models.CharField(max_length=20)
    gisdelte = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=200)
    gstore = models.IntegerField()
    gcontent = HTMLField(default=100)
    gtype = models.ForeignKey('TypeInfo')
