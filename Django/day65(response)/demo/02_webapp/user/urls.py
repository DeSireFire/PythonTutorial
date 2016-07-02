from django.conf.urls import include, url
from user.views import *


urlpatterns=[
    url(r'^register$',register,name='register'),
    url(r'^register_handler$',register_handler,name='register_handler')
]
