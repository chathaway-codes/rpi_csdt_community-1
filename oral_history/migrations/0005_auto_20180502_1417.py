# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oral_history', '0004_auto_20180502_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oralhistory',
            old_name='is_classroom',
            new_name='is_official',
        ),
    ]
