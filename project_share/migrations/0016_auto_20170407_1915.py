# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-07 23:15
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations

import project_share.models


class Migration(migrations.Migration):

    dependencies = [
        ('project_share', '0015_auto_20170407_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='when_requested',
            field=project_share.models.AutoDateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='approval',
            name='when_updated',
            field=project_share.models.AutoDateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='when_created',
            field=project_share.models.AutoDateTimeField(default=django.utils.timezone.now, verbose_name=b'Created'),
        ),
        migrations.AlterField(
            model_name='project',
            name='when_modified',
            field=project_share.models.AutoDateTimeField(default=django.utils.timezone.now, verbose_name=b'Last Changed'),
        ),
    ]
