from django.contrib import admin

# Register your models here.
from .models import Director

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'role', 'team_type', 'gender', 'created_at', 'updated_at'
    )
    list_filter = ('team_type', 'gender')
    search_fields = ('name', 'role', 'bio')
    ordering = ('team_type', 'name')
    fieldsets = (
        (None, {
            'fields': (
                'name', 'role', 'bio', 'photo', 'team_type', 'gender'
            )
        }),
        ('Social Links', {
            'fields': (
                'facebook_url', 'twitter_url', 'instagram_url',
                'linkedin_url', 'skype_url', 'youtube_url'
            ),
            'classes': ('collapse',),  # optional: collapses social links for tidy look
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

