from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'contact', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active')}
         ),
    )

class FooterAdmin(admin.ModelAdmin):
    list_display = ('left_text', 'newsletter_text', 'contact_address', 'contact_phone', 'contact_email', 'contact_website', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'skype_url', 'youtube_url', 'created_at', 'updated_at')


admin.site.register(CustomUser, CustomUserAdmin) 
admin.site.register(Footer, FooterAdmin)