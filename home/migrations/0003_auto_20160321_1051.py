# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160321_1050'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExUserProfile',
            new_name='Group',
        ),
    ]
