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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('deptno', models.AutoField(verbose_name='deptno', primary_key=True, serialize=False, auto_created=True)),
                ('dname', models.CharField(blank=True, null=True, max_length=14, db_column='DNAME')),
                ('loc', models.CharField(blank=True, null=True, max_length=13, db_column='LOC')),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.AutoField(verbose_name='EMPNO', primary_key=True, serialize=False, auto_created=True)),
                ('ename', models.CharField(blank=True, null=True, max_length=14, db_column='ENAME')),
                ('job', models.CharField(blank=True, null=True, max_length=9, db_column='JOB')),
                ('hiredate', models.DateField(blank=True, null=True, db_column='HIREDATE')),
                ('sal', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7, db_column='SAL')),
                ('comm', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7, db_column='COMM')),
                ('dept', models.ForeignKey(null=True, blank=True, to='booktest.Dept')),
                ('mgr', models.ForeignKey(null=True, blank=True, to='booktest.Emp')),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hname', models.CharField(max_length=100)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=200)),
                ('isdelete', models.BooleanField()),
                ('hbookinfo', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
