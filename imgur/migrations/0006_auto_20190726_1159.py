# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-26 08:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imgur', '0005_auto_20190723_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img_category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='img_location',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
