from django.contrib import admin
from .models import PreRegistration


@admin.register(PreRegistration)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'specialization', 'level', 'city', 'created_at']
    list_filter = ['specialization', 'level', 'wants_mentor', 'created_at']
    search_fields = ['full_name', 'email', 'city', 'country_of_origin']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Contact', {'fields': ('full_name', 'email', 'phone')}),
        ('Profil', {'fields': ('specialization', 'level', 'country_of_origin', 'city')}),
        ('Préférences', {'fields': ('wants_mentor', 'wants_newsletter')}),
    )
