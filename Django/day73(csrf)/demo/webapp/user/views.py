from django.shortcuts import render,redirect
from user.models import  *
from hashlib import *
from django.http import *
from django.template import loader,RequestContext
from django.core.urlresolvers import reverse
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def register(request):
    return render(request, 'user/register.html')


def register_handler(request):
    user = User()
    user.uname = request.POST.get('username')
    user.upwd = sha1(request.POST.get('userpwd').encode('utf-8')).hexdigest()
    user.save()
    return render(request, 'user/success.html')


def login(request):
    print('session:%s'%request.session.get('currentUser'))

    context = {}
    #获取cookie
    username = request.COOKIES.get('mycooki')
    if username:
        context['username']=username
    return render(request, 'user/login.html',context)

#@csrf_exempt
def login_handler(request):
    #定义上下文
    context={}
    #用户名密码
    username = request.POST.get('username')
    userpwd = sha1(request.POST.get('userpwd').encode('utf-8')).hexdigest()

    #匹配
    ret = User.objects.filter(uname=username,upwd=userpwd)
    if len(ret)==0:
        return HttpResponseRedirect('/user/login')
    else:
        #在服务端保持一个session键值对
        request.session['currentUser'] = username
        request.session.set_expiry(36000)
        #request.session.set_expiry(timedelta(days=2))

        #加载模板
        t1 = loader.get_template('user/success.html')
        #上下文
        requestcontext = RequestContext(request,context)
        #创建具有模板和上下文的reponse
        response = HttpResponse(t1.render(requestcontext))
        #记录用户名密码的变量
        rememberName = request.POST.get('rememberName')
        #判断
        if rememberName=='1':
            #写cookie
            response.set_cookie('mycookie',username,max_age=3600)
        return response





def test1(request):
    context = {'name':'<h1>laowang</h1>'}
    return render(request, 'user/test1.html',context)
    #return HttpResponse('<h1>laowang</h1>')