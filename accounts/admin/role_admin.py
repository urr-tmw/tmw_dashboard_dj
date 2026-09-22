# accounts/admin/role_admin.py

from django.contrib import admin

from accounts.models import Role


class RolePermissionInline(admin.TabularInline):
    """
    Shows assigned permissions inline inside the Role detail page.
    """
    model = Role.permissions.through
    extra = 0
    verbose_name = "Permission"
    verbose_name_plural = "Assigned Permissions"


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "role_name",
        "role_code",
        "is_active",
        "permission_count",
        "created_at",
    )

    search_fields = (
        "role_name",
        "role_code",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "role_name",
    )

    filter_horizontal = (
        "permissions",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 25

    def permission_count(self, obj):
        return obj.permissions.count()

    permission_count.short_description = "Permissions"
