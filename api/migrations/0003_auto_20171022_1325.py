# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171022_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('note', models.TextField()),
                ('time_stamp', models.DateField(auto_now=True)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Lesson')),
            ],
        ),
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
    ]
