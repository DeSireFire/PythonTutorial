from django.shortcuts import *
from django.http import *
from webapp.settings import ips

class MyException(object):
    def process_exception(request,response,exception):
        #记录错误日志
        #自定义错误视图
        return HttpResponse(exception)

    # def process_response(self,request, response):
    #     print('process_response.............')
    #     return response


class MyFilterIp(object):
    def process_request(self,request):
        ip = request.META['REMOTE_ADDR']
        if ip in ips:
            return HttpResponseForbidden('forbidden')