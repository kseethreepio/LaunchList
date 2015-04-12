from django.db import models

class missiontarget(models.Model):
    name_missiontarget   = models.TextField(blank=True)
    desc_missiontarget   = models.TextField(blank=True)
    stat_m_size          = models.SmallIntegerField(null=True)
    stat_m_deltav        = models.DecimalField(max_digits=8, decimal_places=3)
    stat_m_sciencescore  = models.SmallIntegerField(null=True)

class spacecraft(models.Model):
    name_spacecraft      = models.TextField(blank=True)
    desc_spacecraft      = models.TextField(blank=True)
    spacecraftclass      = models.TextField(blank=True)
    stat_sc_mass         = models.SmallIntegerField(null=True)
    stat_sc_size         = models.TextField(blank=True)
    stat_sc_cost         = models.BigIntegerField(null=True)
    stat_sc_buildtime    = models.SmallIntegerField(null=True)
    stat_sc_mmtime       = models.SmallIntegerField(null=True)
    stat_sc_sciencescore = models.SmallIntegerField(null=True)

class launchvehicle(models.Model):
    name_launchvehicle   = models.TextField(blank=True)
    desc_launchvehicle   = models.TextField(blank=True)
    stat_lv_cost         = models.BigIntegerField(null=True)
    stat_lv_gto          = models.SmallIntegerField(null=True)