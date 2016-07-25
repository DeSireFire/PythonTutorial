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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
                ('deptno', models.AutoField(auto_created=True, verbose_name='deptno', serialize=False, primary_key=True)),
                ('dname', models.CharField(db_column='DNAME', blank=True, null=True, max_length=14)),
                ('loc', models.CharField(db_column='LOC', blank=True, null=True, max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.AutoField(auto_created=True, verbose_name='EMPNO', serialize=False, primary_key=True)),
                ('ename', models.CharField(db_column='ENAME', blank=True, null=True, max_length=14)),
                ('job', models.CharField(db_column='JOB', blank=True, null=True, max_length=9)),
                ('hiredate', models.DateField(db_column='HIREDATE', blank=True, null=True)),
                ('sal', models.DecimalField(db_column='SAL', max_digits=7, blank=True, null=True, decimal_places=2)),
                ('comm', models.DecimalField(db_column='COMM', max_digits=7, blank=True, null=True, decimal_places=2)),
                ('dept', models.ForeignKey(blank=True, to='booktest.Dept', null=True)),
                ('mgr', models.ForeignKey(blank=True, to='booktest.Emp', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('hname', models.CharField(max_length=100)),
                ('hgender', models.BooleanField()),
                ('hcontent', tinymce.models.HTMLField()),
                ('isdelete', models.BooleanField()),
                ('hbookinfo', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
