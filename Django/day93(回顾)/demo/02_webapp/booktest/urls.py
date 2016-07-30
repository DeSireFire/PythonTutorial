from django.conf.urls import include, url
from booktest.views import *

urlpatterns=[
    url(r'^books$',books,name='books'),
    url(r'^books_page$',books_page,name='books_page'),
    url(r'^(?P<id>\d+)$',bookdetail,name='bookdetail'),
    url(r'^add$',add,name='add'),
    url(r'^add_handler$',add_handler,name='add_handler'),
    url(r'^hero_add$',hero_add,name='hero_add'),
    url(r'^hero_add_handler$',hero_add_handler,name='hero_add_handler'),
    url(r'^hero_edit$',hero_edit,name='hero_edit'),
    url(r'^hero_edit_handler$',hero_edit_handler,name='hero_edit_handler'),
    url(r'^hero_show$',hero_show,name='hero_show'),
    url(r'^hero_delete$',hero_delete,name='hero_delete'),
]
