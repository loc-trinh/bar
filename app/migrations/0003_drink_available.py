# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161222_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
