# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Employee, Credit, Invoice, Analytics


# Register your models here.
admin.site.register(Employee)
admin.site.register(Credit)
admin.site.register(Invoice)
admin.site.register(Analytics)