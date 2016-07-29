from django.conf.urls import include, url
from three.views import *


urlpatterns=[
    url(r'^show$',show,name='show'),
    url(r'^get_all_province$',get_all_province,name='get_all_province'),
    url(r'^get_city_by_pid$',get_city_by_pid,name='get_city_by_pid'),
    url(r'^get_area_by_cid$',get_area_by_cid,name='get_area_by_cid'),
]
