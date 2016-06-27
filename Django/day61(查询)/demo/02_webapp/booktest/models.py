from django.db import models






class BookInfo(models.Model):
    btitle = models.CharField(max_length=100)
    bpubdate = models.DateField()
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isdelete = models.BooleanField()

    def __str__(self):
        return self.btitle





class HeroInfo(models.Model):
    hname = models.CharField(max_length=100)
    hgender = models.TextField()
    hbookinfo = models.ForeignKey(BookInfo)
    hcontent = models.CharField(max_length=200)
    isdelete = models.BooleanField()




class Dept(models.Model):
    deptno = models.IntegerField(db_column='DEPTNO', primary_key=True)
    dname = models.CharField(db_column='DNAME', max_length=14, blank=True, null=True)
    loc = models.CharField(db_column='LOC', max_length=13, blank=True, null=True)



class Emp(models.Model):
    empno = models.IntegerField(db_column='EMPNO', primary_key=True)
    ename = models.CharField(db_column='ENAME', max_length=14, blank=True, null=True)
    job = models.CharField(db_column='JOB', max_length=9, blank=True, null=True)
    mgr = models.ForeignKey('self',db_column='mgr', blank=True, null=True)
    hiredate = models.DateField(db_column='HIREDATE', blank=True, null=True)
    sal = models.DecimalField(db_column='SAL', max_digits=7, decimal_places=2, blank=True, null=True)
    comm = models.DecimalField(db_column='COMM', max_digits=7, decimal_places=2, blank=True, null=True)
    deptno = models.ForeignKey(Dept, db_column='DEPTNO', blank=True, null=True)






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