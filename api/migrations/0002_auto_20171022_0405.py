# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sub_grade',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
