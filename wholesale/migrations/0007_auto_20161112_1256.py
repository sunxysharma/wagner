# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-12 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholesale', '0006_auto_20161112_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newrelease',
            name='image',
            field=models.ImageField(null='True', upload_to='wholesale/media/images/'),
        ),
    ]
