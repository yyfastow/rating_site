# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-19 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliach_rating', '0003_auto_20160518_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sluchim',
            name='phone',
            field=models.CharField(default='999-999-99999', max_length=35),
        ),
    ]
