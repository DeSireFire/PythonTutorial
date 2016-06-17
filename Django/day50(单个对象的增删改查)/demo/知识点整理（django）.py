Django的使用：

django-admin startproject webapp
创建项目

manage.py：一个命令行工具，可以使你用多种方式对Django项目进行交互
内层的目录test1：项目的真正的Python包
_init _.py：一个空文件，它告诉Python这个目录应该被看做一个Python包
settings.py：项目的配置
urls.py：项目的URL声明
wsgi.py：项目与WSGI兼容的Web服务器入口

创建应用的命令：
python manage.py startapp booktest

.
├── booktest
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── webapp
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   └── settings.cpython-35.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py


>>设计内容

>>激活模型：编辑settings.py文件，将booktest应用加入到installed_apps中
	INSTALLED_APPS = (
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'booktest',
	)
>>生成迁移文件：根据模型类生成sql语句，迁移文件被生成到应用的migrations目录
python manage.py makemigrations
.
├── booktest
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-35.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   └── models.cpython-35.pyc
│   ├── tests.py
│   └── views.py
├── manage.py
└── webapp
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   └── settings.cpython-35.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py

>>执行迁移：执行sql语句生成数据表
python manage.py migrate
*****************************

Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: sessions, booktest, admin, contenttypes, auth
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying booktest.0001_initial... OK
  Applying sessions.0001_initial... OK

*****************************
>>完成，然后开始具体需求的实现。
关于代码实现增删改查
流程添加信息>save保存>objects.get()逐个获取>objects.all()获取全部>
********************************
emp = EMP()
emp.ENAME='赤城'
emp.JOB = '员工'
emp.MGR = '011'
emp.HIREDATE = datetime(year=2010,month=10,day=21)
emp.SAL = '5000'
emp.COMM = '1200'
emp.DEPTNO = '01'
emp.save()

empinfo = EMP.objects.get(pk = 1)
empinfo = EMP.objects.all()
********************************
>>创建一个管理员用户
python manage.py createsuperuser

>>启动django服务器
python manage.py runserver 192.168.14.44:5360


>>编辑settings.py文件，设置编码、时区
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'


创建项目和应用流程总结：
>> django-admin startproject Deptapp
创建一个名为Deptapp的项目
项目文件夹下会生成一个项目同名的文件夹和manage.py
项目同名的文件夹里包含项目文件：
.
├── __init__.py
├── settings.py
├── urls.py
└── wsgi.py


>> python manage.py startapp workers
创建一个名为workers的应用
生成一个名为workers的应用文件夹，该文件夹跟manage.py同级
workers应用文件夹内包括文件：
├── admin.py
├── apps.py
├── __init__.py
├── models.py
├── tests.py
├── urls.py
└── views.py

>>创建web模板文件夹Templates
在项目文件夹根目录下创建（注意不是同名的项目配置文件夹下）
推荐在Templates文件夹下创建次级文件夹，方便给HTML文件分类
.
├── Deptapp
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── Templates
│   └── Dept
│       ├── Deptinfo.html
│       └── Depts.html
└── workers



>> 修改settings.py,设置杂项
INSTALLED_APPS的最末添加应用名，如：
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'workers',
]

ALLOWED_HOSTS = ['*']
为ALLOWED_HOSTS添加'*'或'localhost','127.0.0.1',本机IP等
用于规避某些类似"addhost有关"的报错

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
设置编码、时区

如需要更换数据库：
以mysql为例：
注释掉原有DATABASES所有内容
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
改为：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Depts', # Depts为mysql里的数据库，必须提前创建
        'USER': 'root', #登录数据库用户
        'PASSWORD': 'root', #登录数据库用户
        'HOST': '127.0.0.1', #m数据库地址
        'PORT': '3306', #数据库端口号
    }
}

修改TEMPLATES的DIRS设置，用于路径找到之前创建的Templates文件夹
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Templates')], #'Templates'为你的创建文件夹名
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

>>在应用配置文件models.py里添加内容，设计表等
以下举例：
**********************************************************
import django.db
import django.db.models

# Create your models here.
class EMP(django.db.models.Model):
    empno = django.db.models.IntegerField(db_column='雇员编号')
    ename = django.db.models.CharField(max_length=10,db_column='雇员姓名')
    job = django.db.models.CharField(max_length=9,db_column='工作职位')
    mgb = django.db.models.IntegerField(null=True,db_column='雇员领导编号')
    hiredate = django.db.models.DateField(auto_now=True,db_column='雇佣日期')
    sal = django.db.models.DecimalField(max_digits=7, decimal_places=2,db_column='工资')
    comm = django.db.models.DecimalField(max_digits=7, decimal_places=2,db_column='奖金')
    deptno= django.db.models.DecimalField(max_digits=2,decimal_places=0,null=True,db_column='部门编号')
    department= django.db.models.ForeignKey('DEPT',null=True)

    def __str__(self):
        return self.ename

    def cnempno(self):
        return self.empno

    def cnename(self):
        return self.ename

    def cnjob(self):
        return self.job

    def cnmgb(self):
        return self.mgb

    def cnhiredate(self):
        return self.hiredate

    def cnsal(self):
        return self.sal

    def cncomm(self):
        return self.comm

    def cndeptno(self):
        return self.deptno

    def cndepartment(self):
        return self.department
    cnempno.short_description = '员工编号'
    cnename.short_description = '姓名'
    cnjob.short_description = '所属部门'
    cnmgb.short_description = '上司编号'
    cnhiredate.short_description = '雇佣时间'
    cnsal.short_description = '工资'
    cncomm.short_description = '奖金'
    cndeptno.short_description = '部门编号'
    cndepartment.short_description = '部门名称'

class DEPT(django.db.models.Model):
    deptno = django.db.models.IntegerField(db_column='部门编号')
    dname = django.db.models.CharField(max_length=14,db_column='部门名称')
    loc = django.db.models.CharField(max_length=13,db_column='部门位置')

    def __str__(self):
        return self.dname

    def cndeptno(self):
        return self.deptno

    def cndname(self):
        return self.dname

    def cnloc(self):
        return self.loc
    cndeptno.short_description = '部门编号'
    cndname.short_description = '部门名称'
    cnloc.short_description = '部门位置'

class SALGRADE(django.db.models.Model):
    grade = django.db.models.IntegerField(db_column='等级名称')
    losal = django.db.models.IntegerField(db_column='普通工资')
    hisal = django.db.models.IntegerField(db_column='领导工资')

    def __str__(self):
        return self.grade

    def cngrade(self):
        return self.grade

    def cnlosal(self):
        return self.losal

    def cnhisal(self):
        return self.hisal

    cngrade.short_description = '等级名称'
    cnlosal.short_description = '普通工资'
    cnhisal.short_description = '领导工资'
**********************************************************

>>在应用配置文件admin.py里添加内容，用于编辑django的admin页面
【注意】导入应用里的models配置文件。【注意】导入的路径
**********************************************************
from django.contrib import admin
from workers.models import *
# Register your models here.
class EMP_ModelAdmin(admin.ModelAdmin):
    list_display = ['cnempno', 'cnename', 'cnjob','cnmgb','cnhiredate','cnsal','cncomm','cndeptno','cndepartment']
    # 右侧显示的过滤
    list_filter = ['ename', 'department']
    # 搜索条件
    search_fields = ['deptno']
    # 分页
    list_per_page = 2

class EMPInfoInline(admin.StackedInline):
    model = EMP
    extra = 2
    list_display = ['cnempno', 'cnename', 'cnjob','cnmgb','cnhiredate','cnsal','cncomm','cndeptno','cndepartment']

class DEPTInfo_ModelAdmin2(admin.ModelAdmin):
    inlines = [EMPInfoInline]
    list_display = ['cndeptno','cndname','cnloc']


class SALGRADE_ModelAdmin(admin.ModelAdmin):
    list_display = ['cngrade','cnlosal','cnhisal']


admin.site.register(EMP,EMP_ModelAdmin)
admin.site.register(DEPT,DEPTInfo_ModelAdmin2)
admin.site.register(SALGRADE)
**********************************************************

>>在虚拟配置环境下安装pymysql(不换数据库的忽略)
打开终端，pip3 list（python2为pip list）查询是否安装了pymysql()

>>生成迁移文件
>>迁移文件
>>创建超级用户
>>简单验证
>>Templates文件夹的次级文件夹下创建HTML文件
>>创建应用配置文件urls.py
>>修改项目配置文件urls.py


def mytest():
	

附录：
models.Model
[模型组].[模型]
models.CharField()
[模型组].[类型域]
models.BooleanField()
[模型组].[布尔域]
models.ForeignKey('')
[模型组].[外部关键字约束]
