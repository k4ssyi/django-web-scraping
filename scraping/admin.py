# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
