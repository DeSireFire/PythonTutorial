from django.shortcuts import render
from user.models import  *
from hashlib import *
from django.http import *
from django.template import loader,RequestContext

# Create your views here.
def register(request):
    return render(request, 'user/register.html')


def register_handler(request):
    print('request.GET=%s' % (request.GET))
    #print('request.POST=%s' % (request.POST))

    print('-----------')
    print(type(request.GET.get('username')))
    #print(request.POST.get('userpwd'))
    print(request.GET.get('hobby'))
    print(request.GET.getlist('hobby'))
    print(request.GET.getlist('hossbby',['x']))
    print('-----------')

    #user = User()
    #user.uname = request.GET.get('username')s
    #user.upwd = sha1(request.GET.get('userpwd').encode('utf-8')).hexdigest()


    #user.save()

    return render(request, 'user/success.html')



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




def login(request):
    context = {}
    #获取cookie
    #print(request.COOKIES)
    username = request.COOKIES.get('mycooki')
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
        context['msg'] = '用户名密码不匹配'
        #return render(request, 'user/login.html', context)
        return login(request)
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
            response.set_cookie('mycooki',username,max_age=3600)

        return response

