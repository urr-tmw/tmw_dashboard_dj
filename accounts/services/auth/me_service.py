from accounts.models import Employee
from common.constants import (
    SUPER_ADMIN_PERMISSION,
    SYSTEM_ADMIN_ROLE_CODE,
    SYSTEM_ADMIN_ROLE_NAME,
)


class MeService:
    """
    Returns the authenticated user's profile.
    """

    @staticmethod
    def get_profile(user):

        # -----------------------------
        # System Administrator
        # -----------------------------
        if user.is_superuser:

            return {
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_superuser": user.is_superuser,
                    "is_staff": user.is_staff,
                },
                "employee": None,
                "roles": [
                    {
                        "id": 0,
                        "role_name": SYSTEM_ADMIN_ROLE_NAME,
                        "role_code": SYSTEM_ADMIN_ROLE_CODE,
                    }
                ],
                "permissions": [
                    SUPER_ADMIN_PERMISSION
                ],
            }

        # -----------------------------
        # Employee
        # -----------------------------
        employee = user.employee_profile

        roles = list(
            employee.roles.values(
                "id",
                "role_name",
                "role_code",
            )
        )

        permissions = list(
            employee.roles
            .values_list(
                "permissions__permission_code",
                flat=True,
            )
            .distinct()
        )

        return {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_superuser": user.is_superuser,
                "is_staff": user.is_staff,
            },
            "employee": {
                "id": employee.id,
                "employee_code": employee.employee_code,
                "department": employee.department.dept_name,
                "designation": employee.designation.designation_name,
                "dashboard_access": employee.dashboard_access,
                "employee_status": employee.employee_status,
            },
            "roles": roles,
            "permissions": permissions,
        }