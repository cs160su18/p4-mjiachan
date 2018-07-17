# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display/$', views.display, name='display'),
    url(r'^customer/$', views.customer, name='customer'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

