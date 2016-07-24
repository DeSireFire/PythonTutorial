from django.contrib import admin
from booktest.models import *

# Register your models here.

class BookInfo_ModelAdmin(admin.ModelAdmin):
    #显示哪些列
    list_display = ['pk','btitle','bpubdate']
    #右侧显示的过滤
    #list_filter = ['btitle','bpubdate']
    #搜索条件
    #search_fields = ['bpubdate']
    #分页
    #list_per_page = 2

    #按顺序显示
    #fields = ['pk','btitle','bpubdate']
    #分组显示
    # fieldsets = [
    #     ('a',{'fields':['btitle']}),
    #     ('b', {'fields': ['bpubdate']})
    # ]



class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 3

class BookInfo_ModelAdmin2(admin.ModelAdmin):
    inlines = [HeroInfoInline]



class HeroInfo_ModelAdmin(admin.ModelAdmin):
    list_display = ['pk','myhgender','myhname']




#admin.site.register(BookInfo,BookInfo_ModelAdmin)
#admin.site.register(BookInfo,BookInfo_ModelAdmin2)
#admin.site.register(HeroInfo,HeroInfo_ModelAdmin)


admin.site.register(HeroInfo)
admin.site.register(BookInfo)


