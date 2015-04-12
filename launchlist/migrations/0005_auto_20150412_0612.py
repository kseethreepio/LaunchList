# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launchlist', '0004_auto_20150412_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launchvehicle',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='missiontarget',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='spacecraft',
            name='id',
            field=models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True),
        ),
    ]
