# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
# Create your models here.
class m_pengajuan(models.Model):
    id = models.AutoField(primary_key=True)
    nis = models.IntegerField()
    nama = models.CharField(max_length=60)
    nohp = models.CharField(max_length=60)
    item = models.IntegerField()
    jabatan = models.CharField(max_length=60)
    kegunaan = models.CharField(max_length=60)
    flag = models.IntegerField()
    tanggal = models.DateField(blank=True, null=True)
    waktu = models.TimeField(blank=True, null=True)
    timestamp = models.DateTimeField(default=datetime.now)

class m_inventory(models.Model):
    id = models.AutoField(primary_key=True)
    kategori = models.CharField(max_length=60)
    lokasi = models.CharField(max_length=60)
    nama = models.CharField(max_length=60)

class m_user(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    jabatan = models.CharField(max_length=60)