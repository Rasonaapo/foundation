from django.contrib import admin

# Register your models here.
from .models import *

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)

admin.site.register(ContactMessage, ContactMessageAdmin)