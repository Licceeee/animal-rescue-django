from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    autocomplete_fields = ('groups',)
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ['last_login', 'date_joined', 'is_superuser', 'password']
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone',
                    'is_staff', 'get_groups', 'is_active', 'last_login')
