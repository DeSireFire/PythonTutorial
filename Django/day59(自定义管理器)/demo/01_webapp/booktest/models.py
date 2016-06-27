from django.db import models
from django.db.models.manager import Manager


"""
自定义管理器
"""
class BookInfo_Manager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isdelete=0)


class BookInfo(models.Model):
    btitle = models.CharField(max_length=100)
    bpubdate = models.DateField()
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isdelete = models.BooleanField()

    bookinfo_manager1 = Manager()
    bookinfo_manager2 = BookInfo_Manager()


    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=100)
    hgender = models.TextField()
    hbookinfo = models.ForeignKey(BookInfo)
    hcontent = models.CharField(max_length=200)
    isdelete = models.BooleanField()











"""
    class Meta():
        db_table = 'bookinfo22222222222222222222222'
        ordering = ['a']


    def myhgender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    def myhname(self):
        return self.hname

    myhgender.short_description = '性别'
    myhname.short_description = '姓名'
"""