from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'display_name', 'date_joined')

admin.site.register(CustomUser, UserAdmin)



