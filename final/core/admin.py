from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Rate)

@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'ip_addr')

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','name','is_active','rate')

