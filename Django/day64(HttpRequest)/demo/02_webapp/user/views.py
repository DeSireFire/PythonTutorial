from django.shortcuts import render
from user.models import  *
from hashlib import *

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
