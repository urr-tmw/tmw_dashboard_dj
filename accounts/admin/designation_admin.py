from django.contrib import admin

from accounts.models import Designation


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "designation_name",
        "designation_code",
        "department",
        "is_active",
        "created_at",
    )

    search_fields = (
        "designation_name",
        "designation_code",
        "department__dept_name",
    )

    list_filter = (
        "department",
        "is_active",
    )

    ordering = (
        "department",
        "designation_name",
    )

    autocomplete_fields = (
        "department",
    )

    list_per_page = 25