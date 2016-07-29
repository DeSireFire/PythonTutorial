from django.shortcuts import *
from django.http import *
from three.models import *
from django.core import serializers

# 跳转到show.html
def show(request):
    return render(request, 'three/show.html')

# 获取所有的省份,转成json
def get_all_province(request):
    province_list = Province.objects.all()
    content={
        'province_list':serializers.serialize('json',province_list)
    }
    return JsonResponse(content)

# 根据省份的id获取下面的城市,转成json
def get_city_by_pid(request):
    province_id = request.GET.get('province_id')
    city_list = City.objects.filter(cprovince_id=province_id)
    content = {
        'city_list': serializers.serialize('json', city_list)
    }
    return JsonResponse(content)

# 根据城市的id获取下面的区,转成json
def get_area_by_cid(request):
    city_id = request.GET.get('city_id')
    area_list = Area.objects.filter(acity_id=city_id)
    content = {
        'area_list': serializers.serialize('json', area_list)
    }
    return JsonResponse(content)