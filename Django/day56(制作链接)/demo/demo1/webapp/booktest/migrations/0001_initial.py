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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('btitle', models.CharField(max_length=100)),
                ('bpubdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('hname', models.CharField(max_length=100)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=200)),
                ('hbookinfo', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
