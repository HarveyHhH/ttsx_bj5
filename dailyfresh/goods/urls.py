from django.conf.urls import url
from . import views
from .search_view import MySearchView


urlpatterns = [
    url(r'^$', views.index),
    # 链接至商品列表页，前一个（\d+）为typeinfo类的，后一个为goodsinfo类的
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^(\d+)/$', views.detail),
    # ajax方法跟进人气、价格点击事件的数据更新
    # url(r'^list_check/$',views.list_check),
    url(r'^search/?$',MySearchView.as_view()),
]