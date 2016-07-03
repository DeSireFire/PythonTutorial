from django.shortcuts import render,redirect
from user.models import  *
from hashlib import *
from django.http import *
from django.template import loader,RequestContext
from django.core.urlresolvers import reverse

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
    context = {}
    #获取cookie
    username = request.COOKIES.get('mycooki')
    username = username.encode('latin-1').decode('utf-8')
    if username:
        context['username']=username
    return render(request, 'user/login.html',context)

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
            username = username.encode('utf-8').decode('latin-1')
            response.set_cookie('mycooki',username,max_age=3600)
        return response






def test1(request):
    response = HttpResponse('<h1>test1...</h1>')
    print(response.content)
    print(response.charset)
    print(response.status_code)

    response.write('<hr/>laowang')
    response.flush()

    return response

def test2(request):
    response = HttpResponse('写cookie')
    response.set_cookie('c1_key','c1_value',max_age=3600)
    return response


def test3(request,a,b):
    response = HttpResponse('a=%s,b=%s'%(a,b))
    return response