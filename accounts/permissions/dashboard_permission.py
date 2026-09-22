# accounts/permissions/dashboard_permission.py

from rest_framework.permissions import BasePermission

from accounts.services.auth.permission_service import PermissionService


class DashboardPermission(BasePermission):
    """
    Database-driven RBAC permission class.

    Each view declares a permission_map that maps HTTP methods
    to permission strings:

        permission_map = {
            "GET":    DepartmentPermission.VIEW,
            "POST":   DepartmentPermission.CREATE,
            "PUT":    DepartmentPermission.UPDATE,
            "PATCH":  DepartmentPermission.UPDATE,
            "DELETE": DepartmentPermission.DELETE,
        }

    Flow:
        APIView → DashboardPermission → PermissionService → Allow / Deny
    """

    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):

        # ----------------------------------------
        # Resolve required permission from the view
        # ----------------------------------------
        permission_map = getattr(view, "permission_map", {})
        required_permission = permission_map.get(request.method)

        # No permission declared for this method → allow
        if not required_permission:
            return True

        # ----------------------------------------
        # Delegate to PermissionService
        # ----------------------------------------
        return PermissionService.has_permission(
            request.user,
            required_permission,
        )