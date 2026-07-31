from django.contrib import admin

# Register your models here.
from django.contrib import admin
from accounts.models.department import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "dept_name",
        "dept_code",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "dept_name",
        "dept_code",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "dept_name",
    )

    list_per_page = 25