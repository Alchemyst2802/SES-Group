# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160321_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asset_Name', models.CharField(max_length=20)),
                ('Asset_Amount', models.FloatField()),
                ('Current_Price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='Asset_Value',
            field=models.FloatField(default=1000000000),
        ),
        migrations.AddField(
            model_name='asset',
            name='Asset_Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Group'),
        ),
    ]
