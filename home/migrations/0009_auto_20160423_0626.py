# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20160410_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransType', models.CharField(max_length=10)),
                ('Volume', models.FloatField(max_length=10)),
                ('PriceAtTrans', models.FloatField(max_length=10)),
                ('CurrentPrice', models.FloatField(max_length=10)),
                ('ByGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group')),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='Asset_Owner',
        ),
        migrations.AlterField(
            model_name='stock',
            name='StockValue',
            field=models.FloatField(max_length=10),
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
        migrations.AddField(
            model_name='transaction',
            name='StockOfTrans',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.Stock'),
        ),
    ]
