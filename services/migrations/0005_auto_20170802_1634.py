# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20170801_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image'),
        ),
    ]
