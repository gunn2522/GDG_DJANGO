from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserChangeForm


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = UserChangeForm
    model = User

    list_display = ('username', 'email', 'erp_number', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'erp_number', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'erp_number', 'email', 'role', 'password1', 'password2'),
        }),
    )

    search_fields = ('username', 'erp_number', 'email')
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
