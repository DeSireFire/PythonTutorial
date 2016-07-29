# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('aname', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cname', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pname', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='cprovince',
            field=models.ForeignKey(to='three.Province'),
        ),
        migrations.AddField(
            model_name='area',
            name='acity',
            field=models.ForeignKey(to='three.City'),
        ),
    ]
