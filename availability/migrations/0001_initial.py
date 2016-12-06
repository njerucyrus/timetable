# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-28 12:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13)),
                ('lecture_code', models.CharField(max_length=20, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LecturerAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=15)),
                ('from_hr', models.CharField(max_length=10, null=True)),
                ('to_hr', models.CharField(max_length=10, null=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='availability.Lecturer')),
            ],
        ),
    ]