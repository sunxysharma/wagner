# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-16 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholesale', '0012_auto_20161116_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colour_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
