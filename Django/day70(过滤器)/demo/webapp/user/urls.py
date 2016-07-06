from django.conf.urls import include, url
from user.views import *


urlpatterns=[
    url(r'^register$',register,name='register'),
    url(r'^register_handler$',register_handler,name='register_handler'),
    url(r'^login$', login, name='login'),
    url(r'^login_handler$', login_handler, name='login_handler'),
    url(r'^test1$',test1),
    url(r'^test2$',test2),
    url(r'^test3/(\d+)/(\d+)$',test3,name='test3'),
    url(r'^test4$',test4),
]
