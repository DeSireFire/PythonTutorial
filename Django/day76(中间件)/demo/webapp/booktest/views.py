from django.shortcuts import render,redirect
from django.http import HttpResponse
from booktest.models import *



def books(request):
    #获取session
    currentUser = request.session.get('currentUser')
    #判断，如果找不到，去登录
    if not currentUser:
        return redirect('/user/login')


    bookinfo_list = BookInfo.objects.all()
    context = {'bookinfo_list':bookinfo_list}
    return render(request,'booktest/books.html',context)

def bookdetail(request,id):
    bookinfo = BookInfo.objects.filter(pk=id)
    if len(bookinfo):
        bookinfo = bookinfo[0]
        heroinfos = bookinfo.heroinfo_set.all()
    else:
        bookinfo = None
        heroinfos = None


    context = {'bookinfo': bookinfo,'heroinfos':heroinfos}
    return render(request, 'booktest/bookdetail.html', context)


