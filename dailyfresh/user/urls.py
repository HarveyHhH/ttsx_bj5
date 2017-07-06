from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^register_log/$', views.register_log),
    url(r'^login_check/$', views.login_check),
    url(r'^center_info/$', views.center_info),
    url(r'^center_order/$', views.center_order),
    url(r'^center_site/$',views.center_site),
]