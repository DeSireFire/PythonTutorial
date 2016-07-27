from django.shortcuts import render,redirect
from user.models import  *
from hashlib import *
from django.http import *
from django.template import loader,RequestContext
from django.core.urlresolvers import reverse
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import  StringIO,BytesIO
import random
import uuid
import os
from time import sleep
from django.conf import settings
from booktest.models import  *
from user import  task


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
    # 定义上下文
    context = {}


    #获取验证码
    userverification = request.POST.get('userverification')
    if userverification==None or request.session['codes'].upper() != userverification.upper():
        context = {'userverification_error':'验证码输入错误'}
        return render(request,'user/login.html',context)


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





def verification(request):
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    #储存验证码字符串
    codes = ''
    # 输出文字:
    for t in range(4):
        code = rndChar()
        codes += code
        draw.text((60 * t + 10, 10),code , font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)


    #将验证码字符串存储到session中
    request.session['codes'] = codes
    request.session.set_expiry(0)

    #内存级的字节读写
    f = BytesIO()
    image.save(f,'jpeg')

    return HttpResponse(f.getvalue(),'image/jpeg')



def check_username(request):
    username = request.GET.get('username')
    # 0不存在   1存在
    ret = '0'
    if len(User.objects.filter(uname=username)):
        ret = '1'
    return HttpResponse(ret)


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def test1(request):
    return render(request, 'user/test1.html')





def test3(request):
    return render(request, 'user/test3.html')

def test4(request):
    id = request.GET.get('id')
    name = request.GET.get('name')

    print('id=%s,name=%s'%(id,name))

    sleep(3)

    return HttpResponse('ok')







def test2(request):
    #接收上传的文件
    file = request.FILES.get('myfile',None)
    #判断
    if file:
        #文件的新名字
        name = doFileName(file.name)
        #拼接路径
        path = os.path.join(settings.MEDIA_ROOT,'images',name)
        #读写文件
        with open(path,'wb') as f:
            for chunk in  file.chunks():
                f.write(chunk)

        #接收其他字段，+name  存到数据库中
        #文件的存放策略
    else:
        pass

    return render(request, 'user/success.html')


#load
def test5(request):
    return render(request, 'user/test5.html')

def test6(request):
    return render(request, 'user/test6.html')

def test7(request):
    return render(request, 'user/test7.html')




def test8(request):
    #模拟耗时的操作
    task.hello_world.delay()
    #task.hello_world()

    return render(request, 'user/test8.html')


