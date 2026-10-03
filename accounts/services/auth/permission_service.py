from accounts.models import Employee


class PermissionService:
    """
    Handles RBAC permission evaluation.
    """

    @staticmethod
    def group_by_module(employee):
        """
        Returns the employee's permissions as one list per module.

        {
            "Department": ["department.view", "department.create"],
            "Employee": ["employee.view"]
        }
        """

        rows = (
            employee.roles
            .order_by(
                "permissions__module",
                "permissions__action",
                "permissions__permission_code",
            )
            .values_list(
                "permissions__module",
                "permissions__permission_code",
            )
            .distinct()
        )

        grouped = {}

        for module, code in rows:
            if not module or not code:
                continue

            codes = grouped.setdefault(module, [])

            if code not in codes:
                codes.append(code)

        return grouped

    @staticmethod
    def has_permission(user, required_permission):
        """
        Returns True if the user has the required permission.
        """

        # -----------------------------
        # Anonymous User
        # -----------------------------
        if not user.is_authenticated:
            return False

        # -----------------------------
        # Super Admin
        # -----------------------------
        if user.is_superuser:
            return True

        try:
            employee = user.employee_profile

        except Employee.DoesNotExist:
            return False

        if not employee.dashboard_access:
            return False

        if employee.employee_status != Employee.EmployeeStatus.ACTIVE:
            return False

        return employee.roles.filter(
            permissions__permission_code=required_permission,
            is_active=True,
            permissions__is_active=True,
        ).exists()