from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as WritersLeagueUserAdmin

from .models import Address, Profile, CustomUser


class ProfileInline(admin.StackedInline):
    model = Profile

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'address2', 'city', 'post_code', 'country')


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'active')


@admin.register(CustomUser)
class UserAdmin(WritersLeagueUserAdmin):
    inlines = [ProfileInline]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
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
