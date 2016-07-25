from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import *
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.paginator import Paginator
import uuid
import os
import time
import  json
from django.core import serializers



def books(request):
    return render(request, 'booktest/books.html')


def books_page(request):
    # 获取当前页码
    pagenow = int(request.GET.get('pagenow'))
    # 每页显示几条
    pageSize = 2
    # 总数据
    resultset = BookInfo.objects.filter(isdelete=0).order_by('pk')
    # 构造Paganitor对象
    paginator = Paginator(resultset, pageSize)
    page = paginator.page(pagenow)

    #准备上下文的数据
    content = {
        'bookinfo_list': serializers.serialize('json',page.object_list),
        'page_range': json.dumps(paginator.page_range),
        'pagenow': pagenow
    }
    #return HttpResponse(str(content))
    return JsonResponse(content)


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



def add(request):
    return render(request,'booktest/book_add.html')


def add_handler(request):
    btitle = request.POST.get('btitle')
    bpubdate = request.POST.get('bpubdate')
    bread = request.POST.get('bread')
    bcomment = request.POST.get('bcomment')
    isdelete = request.POST.get('isdelete',0)
    bimage = request.FILES.get('bimage')
    # 文件的新名字
    name = str(uuid.uuid1())+os.path.splitext(bimage.name)[1]
    # 拼接路径
    path = os.path.join(settings.MEDIA_ROOT, 'images', name)
    # 读写文件
    with open(path, 'wb') as f:
        for chunk in bimage.chunks():
            f.write(chunk)

    # 接收其他字段，+name  包装对象存到数据库中
    book = BookInfo()
    book.btitle = btitle
    book.bpubdate = bpubdate
    book.bread = bread
    book.bcomment = bcomment
    book.bimage = name
    book.isdelete = isdelete


    print('isdelete:'+str(isdelete))

    book.save()




    return redirect(reverse('books:books'))