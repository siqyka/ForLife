# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tltie', models.CharField(max_length=54)),
                ('rurl', models.CharField(max_length=54)),
                ('radd', models.CharField(max_length=54)),
                ('geren', models.CharField(max_length=54)),
                ('money', models.CharField(max_length=54)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=54)),
                ('company', models.CharField(max_length=54)),
                ('sadd', models.CharField(max_length=54)),
                ('salary', models.CharField(max_length=54)),
                ('claim', models.CharField(max_length=54)),
                ('joburl', models.CharField(max_length=54)),
            ],
        ),
    ]
