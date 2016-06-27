# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('btitle', models.CharField(max_length=100)),
                ('bpubdate', models.DateField()),
                ('bread', models.IntegerField()),
                ('bcomment', models.IntegerField()),
                ('isdelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, db_column='DEPTNO', serialize=False)),
                ('dname', models.CharField(max_length=14, blank=True, null=True, db_column='DNAME')),
                ('loc', models.CharField(max_length=13, blank=True, null=True, db_column='LOC')),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(primary_key=True, db_column='EMPNO', serialize=False)),
                ('ename', models.CharField(max_length=14, blank=True, null=True, db_column='ENAME')),
                ('job', models.CharField(max_length=9, blank=True, null=True, db_column='JOB')),
                ('hiredate', models.DateField(blank=True, null=True, db_column='HIREDATE')),
                ('sal', models.DecimalField(max_digits=7, blank=True, null=True, decimal_places=2, db_column='SAL')),
                ('comm', models.DecimalField(max_digits=7, blank=True, null=True, decimal_places=2, db_column='COMM')),
                ('deptno', models.ForeignKey(null=True, to='booktest.Dept', blank=True, db_column='DEPTNO')),
                ('mgr', models.ForeignKey(null=True, to='booktest.Emp', blank=True, db_column='mgr')),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('hname', models.CharField(max_length=100)),
                ('hgender', models.TextField()),
                ('hcontent', models.CharField(max_length=200)),
                ('isdelete', models.BooleanField()),
                ('hbookinfo', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
