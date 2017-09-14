from django.contrib import admin
from .models import TypeInfo, GoodsInfo

# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
admin.site.register(TypeInfo,TypeInfoAdmin)


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle']
    list_per_page = 15
admin.site.register(GoodsInfo,GoodsInfoAdmin)
