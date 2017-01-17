# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholesale', '0010_auto_20161114_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newrelease',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newrelease',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='newrelease',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]