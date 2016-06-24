from django.conf.urls import include, url
from booktest.views import *


urlpatterns=[
    url(r'^a/b/c/$',books),
    url(r'^(\d+)$',bookdetail,name='bookdetail')
]
