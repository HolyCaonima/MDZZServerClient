# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Account, Boss, KeFu

admin.site.add_action(Account)
admin.site.add_action(Boss)
admin.site.add_action(KeFu)

