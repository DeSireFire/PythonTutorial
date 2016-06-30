from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import *



def books(request):
    bookinfo_list = BookInfo.objects.all()
    context = {'bookinfo_list':bookinfo_list}
    return render(request,'booktest/books.html',context)




def bookdetail(request,id,num):

    num=1/0

    bookinfo = BookInfo.objects.get(pk=id)
    context = {'bookinfo': bookinfo}
    return render(request, 'booktest/bookdetail.html', context)


