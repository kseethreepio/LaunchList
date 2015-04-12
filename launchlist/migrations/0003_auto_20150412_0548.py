# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launchlist', '0002_auto_20150412_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launchvehicle',
            name='id_launchvehicle',
        ),
        migrations.RemoveField(
            model_name='missiontarget',
            name='id_missiontarget',
        ),
        migrations.RemoveField(
            model_name='spacecraft',
            name='id_spacecraft',
        ),
        migrations.AddField(
            model_name='launchvehicle',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, auto_created=True, default=0, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='missiontarget',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, auto_created=True, default=0, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, auto_created=True, default=0, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
