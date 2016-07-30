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




def hero_add(request):
    #准备数据-书
    book_list = BookInfo.objects.all()
    #上下文字典
    context={
        'book_list':book_list
    }

    return render(request, 'booktest/hero_edit.html',context)


def hero_edit(request):
    #获取id
    id = request.GET.get('id')
    #查询对象
    heroinfo = HeroInfo.objects.get(pk=id)
    #准备数据-书
    book_list = BookInfo.objects.all()
    #上下文字典
    context={
        'book_list':book_list,
        'heroinfo':heroinfo
    }

    return render(request, 'booktest/hero_edit.html',context)


def hero_add_handler(request):
    #接受参数
    hname = request.GET.get('hname')
    hgender = request.GET.get('hgender')
    hcontent = request.GET.get('hcontent')
    hbookinfo_id = request.GET.get('hbookinfo_id')
    hbookinfo = BookInfo.objects.get(pk=hbookinfo_id)

    #包装成对象
    h = HeroInfo()
    h.hgender = hgender
    h.hcontent = hcontent
    h.hname = hname
    h.hbookinfo = hbookinfo
    h.isdelete=0

    #save
    h.save()

    #重定向到查询所有英雄的view
    return redirect('/booktest/hero_show')


def hero_edit_handler(request):
    # 接受参数
    id = request.GET.get('id')
    hname = request.GET.get('hname')
    hgender = int(request.GET.get('hgender'))
    hcontent = request.GET.get('hcontent')
    isdelete = request.GET.get('isdelete',0)
    hbookinfo_id = request.GET.get('hbookinfo_id')
    hbookinfo = BookInfo.objects.get(pk=hbookinfo_id)

    # 查询对象
    h = HeroInfo.objects.get(pk=id)
    # 修改属性
    h.hgender = hgender
    h.hcontent = hcontent
    h.hname = hname
    h.hbookinfo = hbookinfo
    h.isdelete = isdelete

    # update
    h.save()

    # 重定向到查询所有英雄的view
    return redirect('/booktest/hero_show')




#查询所有的影响信息
def hero_show(request):
    hero_list = HeroInfo.objects.filter(isdelete=0)
    context={'hero_list':hero_list}

    print(context)

    return render(request, 'booktest/heros.html', context)

#根据id删除
def hero_delete(request):
    #获取id
    id = request.GET.get('id')
    #查询对象
    h = HeroInfo.objects.get(pk=id)
    #修改
    h.isdelete = 1
    #保存
    h.save()
    # 重定向到查询所有英雄的view
    return redirect('/booktest/hero_show')