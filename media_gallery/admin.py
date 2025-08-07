from django.contrib import admin
from . models import GalleryImage, MarqueeImage
# Register your models here.

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption', 'archived', 'expires_at', 'created_at', 'updated_at')
    list_filter = ('expires_at', 'archived', 'created_at')
    search_fields = ('caption',)
    ordering = ('-created_at',)

class MarqueeImageAdmin(admin.ModelAdmin): 
    list_display = ('image', 'caption', 'order', 'created_at', 'updated_at')
    search_fields = ('caption',)
    ordering = ('-created_at',)

admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(MarqueeImage, MarqueeImageAdmin)