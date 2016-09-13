# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-14 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_scales_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='scales',
            options={'ordering': ['scale_name'], 'verbose_name_plural': 'scales'},
        ),
    ]