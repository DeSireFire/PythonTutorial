#from django.db import models
# Create your models here.

"""
这里的模型类（与数据库表对应的类）
必须继承django.db.models.Model
ORM
"""
"""
create table bookinfo(
     bid int auto_increment primary key,
     btitle varchar(100),
     bpubdate date
);
create table heroinfo(
     hid int auto_increment primary key,
     hname varchar(100),
     hgender bit,
     hcontent longtext,
     bid int,
     foreign key(bid) references bookinfo(bid)
);

"""

import django.db
import django.db.models

class BookInfo(django.db.models.Model):
    btitle = django.db.models.CharField(max_length=100)
    bpubdate = django.db.models.DateField()

    def __str__(self):
        return self.btitle

class HeroInfo(django.db.models.Model):
    hname = django.db.models.CharField(max_length=100)
    hgender = django.db.models.BooleanField()
    hcontent = django.db.models.CharField(max_length=200)
    hbookinfo = django.db.models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname

#HeroInfo 数据库中没有hbookinfo，列名是hbookinfo_id
#BookInfo 数据库中没有HeroInfo_set，HeroInfo_set是管理器帮忙维护的