# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app1.models import jaipurjobs
from django.contrib import admin

# Register your models here.
class jaipurjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','phonenumber']

admin.site.register(jaipurjobs,jaipurjobsAdmin)
