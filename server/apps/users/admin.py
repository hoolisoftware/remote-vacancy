from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            'Personal Info', 
            {
                'fields': (
                    'email', 
                    'first_name', 
                    'last_name',
                    'avatar',
                    'account_type'
                )
            }
        ),
        (
            'Additional Info', 
            {
                'fields': (
                    'last_login', 
                    'date_joined', 
                )
            }
        ),
        (
            'Staff Info', 
            {
                'fields': (
                    'is_active', 
                    'is_staff', 
                    'is_superuser', 
                    'user_permissions', 
                    'groups'
                ), 
                'classes': ('collapse',)
            }
        ),
    )