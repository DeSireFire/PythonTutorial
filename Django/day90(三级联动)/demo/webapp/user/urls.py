from django.conf.urls import include, url
from user.views import *


urlpatterns=[
    url(r'^register$',register,name='register'),
    url(r'^register_handler$',register_handler,name='register_handler'),
    url(r'^login$', login, name='login'),
    url(r'^login_handler$', login_handler, name='login_handler'),
    url(r'^verification$', verification, name='verification'),
    url(r'^check_username$', check_username, name='check_username'),
    url(r'^test1$', test1),
    url(r'^test2$', test2),
    url(r'^test3$', test3),
    url(r'^test4$', test4),
    url(r'^test5$', test5),
    url(r'^test6$', test6),
    url(r'^test7$', test7),
    url(r'^test8$', test8),
]
