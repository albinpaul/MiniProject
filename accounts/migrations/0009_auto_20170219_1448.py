# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170219_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
