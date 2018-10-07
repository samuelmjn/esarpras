# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import m_inventory,m_pengajuan,m_user


# Register your models here.
admin.site.register(m_inventory)
admin.site.register(m_pengajuan)
admin.site.register(m_user)