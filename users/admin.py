from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    model = User

    list_display = (
        'email',
        'number',
        'ward',
        'gender',
        'nid',
        'date_of_birth',
        'address',
        'role',
        'is_active'
    )

    list_filter = ('role', 'is_active')
    ordering = ('email',)
    search_fields = ('number','email')

    # Remove default username field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': (
                'number',
                'ward',
                'gender',
                'nid',
                'date_of_birth',
                'address',
                'role',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Important Dates', {
            'fields': ('last_login',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'number',
                'email',
                'password1',
                'password2',
                'is_active',
                'is_staff',
            ),
        }),
    )