from django.conf.urls import include, url
from booktest.views import *


urlpatterns=[
    url(r'^books$',books,name='books'),
    url(r'^books_page$',books_page,name='books_page'),
    url(r'^(?P<id>\d+)$',bookdetail,name='bookdetail'),
    url(r'^add$',add,name='add'),
    url(r'^add_handler$',add_handler,name='add_handler')
]
