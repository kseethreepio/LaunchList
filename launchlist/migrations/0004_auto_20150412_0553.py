# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launchlist', '0003_auto_20150412_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launchvehicle',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='missiontarget',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spacecraft',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
