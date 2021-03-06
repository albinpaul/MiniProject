# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 04:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionno', models.CharField(max_length=7)),
                ('status', models.CharField(choices=[(b'PC', b'Placement_Cell'), (b'TC', b'Training_Cell'), (b'ST', b'Student')], default=b'ST', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
