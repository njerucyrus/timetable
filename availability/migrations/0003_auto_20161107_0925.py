# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0002_auto_20161028_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecturer',
            old_name='lecture_code',
            new_name='lecturer_code',
        ),
    ]
