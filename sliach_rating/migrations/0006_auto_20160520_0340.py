# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-20 03:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sliach_rating', '0005_auto_20160520_0311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rate',
            new_name='Rating',
        ),
    ]