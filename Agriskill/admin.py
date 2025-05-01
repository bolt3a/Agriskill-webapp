from django.contrib import admin
from .models import Landowner, SkilledProfessional  # Import the specific models

@admin.register(Landowner)
class LandownerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'age', 'mobile_number', 'total_area', 'help_needed', 'district', 'city')
    search_fields = ('full_name', 'email', 'mobile_number', 'district', 'city')
    list_filter = ('district', 'city')  # Allows filtering by district and city


@admin.register(SkilledProfessional)
class SkilledProfessionalAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'age', 'mobile_number', 'skills', 'district', 'city')
    search_fields = ('full_name', 'email', 'mobile_number', 'skills', 'district', 'city')
    list_filter = ('district', 'city')  # Allows filtering by district and city
