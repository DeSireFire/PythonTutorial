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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('btitle', models.CharField(max_length=100)),
                ('bpubdate', models.DateField()),
                ('bread', models.IntegerField()),
                ('bcomment', models.IntegerField()),
                ('isdelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('hname', models.CharField(max_length=100)),
                ('hgender', models.TextField()),
                ('hcontent', models.CharField(max_length=200)),
                ('isdelete', models.BooleanField()),
                ('hbookinfo', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
