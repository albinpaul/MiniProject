# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0014_remove_apt_test_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apt_test',
            name='endDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='test enddate'),
        ),
        migrations.AlterField(
            model_name='apt_test',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
