from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cart/$', views.cart),
    url(r'^add/$', views.cart_add),
    url(r'^count/$', views.count),
    url(r'^index/$', views.index),
    # url(r'^cart_init/$', views.cart_init),
    url(r'^record/$', views.record),
    url(r'^del/$', views.delete),
    # url(r'^dell/$', views.delete2),
]