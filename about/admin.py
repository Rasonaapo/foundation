from django.contrib import admin
from .models import *


class MissionAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'updated_at')
    search_fields = ('text',)
    ordering = ('-created_at',)

class VisionAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'updated_at')
    search_fields = ('text',)
    ordering = ('-created_at',)

class ValueAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Mission, MissionAdmin)
admin.site.register(Vision, VisionAdmin)
admin.site.register(Value, ValueAdmin)