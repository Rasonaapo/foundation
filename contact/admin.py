from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('info_type', 'title', 'icon_class', 'created_at', 'updated_at')
    list_filter = ('info_type',)
    search_fields = ('title', 'description', 'extra_info', 'icon_class')

    fieldsets = (
        (None, {
            'fields': ('info_type', 'title', 'description', 'extra_info', 'icon_class')
        }),
    )