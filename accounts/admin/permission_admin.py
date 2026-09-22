# accounts/admin/permission_admin.py

from django.contrib import admin

from accounts.models import Permission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "module",
        "action",
        "permission_name",
        "permission_code",
        "is_active",
        "created_at",
    )

    search_fields = (
        "module",
        "action",
        "permission_name",
        "permission_code",
    )

    list_filter = (
        "module",
        "is_active",
    )

    ordering = (
        "module",
        "action",
    )

    readonly_fields = (
        "permission_code",
        "permission_name",
        "created_at",
        "updated_at",
    )

    list_per_page = 25