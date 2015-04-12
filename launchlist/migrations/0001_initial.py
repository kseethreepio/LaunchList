# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='launchvehicle',
            fields=[
                ('id_launchvehicle', models.SmallIntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='missiontarget',
            fields=[
                ('id_missiontarget', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('stat_m_deltav', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='spacecraft',
            fields=[
                ('id_spacecraft', models.SmallIntegerField(serialize=False, primary_key=True)),
            ],
        ),
    ]
