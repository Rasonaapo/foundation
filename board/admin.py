from django.contrib import admin

# Register your models here.
from .models import Director

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'bio', 'created_at', 'updated_at')
    search_fields = ('name', 'role')
    ordering = ('name',)

admin.site.register(Director, DirectorAdmin)