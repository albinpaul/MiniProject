# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20170301_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Answers')),
                ('qn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Apt_Qns')),
            ],
        ),
        migrations.RemoveField(
            model_name='options',
            name='qn_id',
        ),
        migrations.DeleteModel(
            name='Options',
        ),
    ]
