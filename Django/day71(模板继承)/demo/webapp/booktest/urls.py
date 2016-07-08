from django.conf.urls import include, url
from booktest.views import *


urlpatterns=[
    url(r'^$',books),
    url(r'^(?P<id>\d+)$',bookdetail,name='bookdetail')
]
