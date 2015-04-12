# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launchlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='launchvehicle',
            name='desc_launchvehicle',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='launchvehicle',
            name='name_launchvehicle',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='launchvehicle',
            name='stat_lv_cost',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='launchvehicle',
            name='stat_lv_gto',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='missiontarget',
            name='desc_missiontarget',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='missiontarget',
            name='name_missiontarget',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='missiontarget',
            name='stat_m_sciencescore',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='missiontarget',
            name='stat_m_size',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='desc_spacecraft',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='name_spacecraft',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='spacecraftclass',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='stat_sc_buildtime',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='stat_sc_cost',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='stat_sc_mass',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='stat_sc_mmtime',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='stat_sc_sciencescore',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spacecraft',
            name='stat_sc_size',
            field=models.TextField(blank=True),
        ),
    ]
