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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'expiry_date', 'archived', 'created_at')
    list_filter = ('archived', 'categories',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories',)
    date_hierarchy = 'event_date'

class MostTrendingAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'expiry_date', 'archived', 'created_at')
    list_filter = ('archived', 'created_at')
    search_fields = ('title', 'url')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(MostTrending, MostTrendingAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(CustomUser, CustomUserAdmin) 
admin.site.register(Footer, FooterAdmin)