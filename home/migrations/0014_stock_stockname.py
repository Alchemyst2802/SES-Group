# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_stock_stockname'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='StockName',
            field=models.CharField(default='asdasd', max_length=100),
            preserve_default=False,
        ),
    ]
