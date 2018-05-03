# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 19:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oral_history', '0006_auto_20180502_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='csdt_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_share.Project'),
        ),
        migrations.AlterField(
            model_name='oralhistory',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='oralhistoryproject/%Y-%m-%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=[b'ppm', b'grib', b'im', b'blp', b'rgba', b'rgb', b'jpx', b'h5', b'jpe', b'jpf', b'jpg', b'fli', b'jpc', b'sgi', b'gbr', b'pcx', b'mpeg', b'jpeg', b'ps', b'flc', b'tif', b'hdf', b'icns', b'gif', b'palm', b'mpg', b'fits', b'pgm', b'mic', b'pxr', b'fit', b'xbm', b'eps', b'emf', b'jp2', b'dcx', b'webp', b'bmp', b'bw', b'pbm', b'j2c', b'psd', b'pcd', b'ras', b'j2k', b'mpo', b'cur', b'fpx', b'ftu', b'png', b'msp', b'iim', b'wmf', b'jfif', b'tga', b'bufr', b'ico', b'ftc', b'xpm', b'pdf', b'dds', b'tiff'])]),
        ),
    ]
