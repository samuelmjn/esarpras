# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-12 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_pengajuan',
            name='tanggal',
            field=models.DateField(blank=True, null=True),
        ),
    ]
