# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_stock_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='StockOfTrans',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Stock'),
        ),
    ]