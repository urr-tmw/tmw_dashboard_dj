from django.contrib import admin

from accounts.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "employee_code",
        "user",
        "department",
        "designation",
        "reporting_manager",
        "dashboard_access",
        "employee_status",
    )

    search_fields = (
        "employee_code",
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )

    list_filter = (
        "department",
        "designation",
        "employee_status",
        "dashboard_access",
    )

    autocomplete_fields = (
        "user",
        "department",
        "designation",
        "reporting_manager",
    )

    ordering = (
        "employee_code",
    )

    list_per_page = 25