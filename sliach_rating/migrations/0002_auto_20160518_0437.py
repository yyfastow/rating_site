# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-18 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliach_rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.CharField(default='USA', max_length=200),
        ),
    ]
