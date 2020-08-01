from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as WritersLeagueUserAdmin

from .models import Address, CustomUser


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'address2', 'city', 'post_code', 'country')


@admin.register(CustomUser)
class UserAdmin(WritersLeagueUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password", "user_type")}),
        ("Personal info", {"fields": ("first_name", "last_name")},),
        # ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",)},),
        # ("Important dates", {"fields": ("last_login", "date_joined")},),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
