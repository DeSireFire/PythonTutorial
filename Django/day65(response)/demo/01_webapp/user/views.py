from django.shortcuts import render
from user.models import  *
from hashlib import *
from django.http import *

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




