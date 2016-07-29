# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('btitle', models.CharField(max_length=100)),
                ('bpubdate', models.DateField(default=django.utils.timezone.now)),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('bimage', models.ImageField(upload_to='images', null=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.AutoField(verbose_name='deptno', primary_key=True, auto_created=True, serialize=False)),
                ('dname', models.CharField(max_length=14, null=True, db_column='DNAME', blank=True)),
                ('loc', models.CharField(max_length=13, null=True, db_column='LOC', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.AutoField(verbose_name='EMPNO', primary_key=True, auto_created=True, serialize=False)),
                ('ename', models.CharField(max_length=14, null=True, db_column='ENAME', blank=True)),
                ('job', models.CharField(max_length=9, null=True, db_column='JOB', blank=True)),
                ('hiredate', models.DateField(null=True, db_column='HIREDATE', blank=True)),
                ('sal', models.DecimalField(null=True, max_digits=7, decimal_places=2, db_column='SAL', blank=True)),
                ('comm', models.DecimalField(null=True, max_digits=7, decimal_places=2, db_column='COMM', blank=True)),
                ('dept', models.ForeignKey(null=True, to='booktest.Dept', blank=True)),
                ('mgr', models.ForeignKey(null=True, to='booktest.Emp', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('hname', models.CharField(max_length=100)),
                ('hgender', models.BooleanField()),
                ('hcontent', tinymce.models.HTMLField()),
                ('isdelete', models.BooleanField()),
                ('hbookinfo', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
