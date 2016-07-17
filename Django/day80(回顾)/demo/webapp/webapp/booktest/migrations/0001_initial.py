# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('btitle', models.CharField(max_length=100)),
                ('bpubdate', models.DateField(default=django.utils.timezone.now)),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('bimage', models.ImageField(null=True, upload_to='images')),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.AutoField(primary_key=True, verbose_name='deptno', serialize=False, auto_created=True)),
                ('dname', models.CharField(db_column='DNAME', blank=True, null=True, max_length=14)),
                ('loc', models.CharField(db_column='LOC', blank=True, null=True, max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.AutoField(primary_key=True, verbose_name='EMPNO', serialize=False, auto_created=True)),
                ('ename', models.CharField(db_column='ENAME', blank=True, null=True, max_length=14)),
                ('job', models.CharField(db_column='JOB', blank=True, null=True, max_length=9)),
                ('hiredate', models.DateField(db_column='HIREDATE', null=True, blank=True)),
                ('sal', models.DecimalField(max_digits=7, db_column='SAL', decimal_places=2, null=True, blank=True)),
                ('comm', models.DecimalField(max_digits=7, db_column='COMM', decimal_places=2, null=True, blank=True)),
                ('dept', models.ForeignKey(to='booktest.Dept', null=True, blank=True)),
                ('mgr', models.ForeignKey(to='booktest.Emp', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('hname', models.CharField(max_length=100)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=200)),
                ('isdelete', models.BooleanField()),
                ('hbookinfo', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
