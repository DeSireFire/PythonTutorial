from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import *



def books(request):
    print('request=%s' % request)
    print('request.path=%s' %(request.path))
    print('request.method=%s' %(request.method))
    print('request.encoding=%s' %(request.encoding))
    print('request.GET=%s' %(request.GET))
    print('request.POST=%s' %(request.POST))


    bookinfo_list = BookInfo.objects.all()
    context = {'bookinfo_list':bookinfo_list}
    return render(request,'booktest/books.html',context)




def bookdetail(request,id):
    bookinfo = BookInfo.objects.get(pk=id)
    context = {'bookinfo': bookinfo}
    return render(request, 'booktest/bookdetail.html', context)

def bookdetail(request,id):
    bookinfo = BookInfo.objects.get(pk=id)
    context = {'bookinfo': bookinfo}
    return render(request, 'booktest/bookdetail.html', context)


def bookregister(request):
    return render(request, 'booktest/bookregister.html')

def bookregister_handler(request):
    print('request.GET=%s' % (request.GET))
    print('request.POST=%s' % (request.POST))

    return render(request, 'booktest/bookregister_handler.html')
