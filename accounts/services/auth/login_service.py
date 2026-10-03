from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import Employee
from accounts.services.auth.menu_service import MenuService
from accounts.services.auth.permission_service import PermissionService
from common.constants import (
    SUPER_ADMIN_PERMISSION,
    SYSTEM_ADMIN_ROLE_NAME,
    SYSTEM_ADMIN_ROLE_CODE,
)
User = get_user_model()


class LoginService:
    """
    Handles dashboard authentication.
    """

    @staticmethod
    def login(validated_data):

        login = validated_data["login"]
        password = validated_data["password"]

        # ------------------------------------------------
        # Username / Email Login
        # ------------------------------------------------

        user = User.objects.filter(
            Q(username__iexact=login) |
            Q(email__iexact=login)
        ).first()

        if not user:
            raise AuthenticationFailed(
                "Invalid username/email or password."
            )

        user = authenticate(
            username=user.username,
            password=password,
        )

        if not user:
            raise AuthenticationFailed(
                "Invalid username/email or password."
            )

        if not user.is_active:
            raise AuthenticationFailed(
                "User account is inactive."
            )
        # ------------------------------------------------
        # System Administrator
        # ------------------------------------------------

        if user.is_superuser:
            refresh = RefreshToken.for_user(user)

            access = refresh.access_token

            permissions = {
                "*": [SUPER_ADMIN_PERMISSION],
            }
            roles = [
                {
                    "id": 0,
                    "role_name": SYSTEM_ADMIN_ROLE_NAME,
                    "role_code": SYSTEM_ADMIN_ROLE_CODE,
                }
            ]

            return {
                "refresh": str(refresh),
                "access": str(access),
                "user": user,
                "employee": None,
                "roles": roles,
                "permissions": permissions,
                "menus": MenuService.build(permissions, roles),
            }
        # ------------------------------------------------
        # Employee Validation
        # ------------------------------------------------

        try:
            employee = user.employee_profile

        except Employee.DoesNotExist:
            raise AuthenticationFailed(
                "Employee profile not found."
            )

        if not employee.dashboard_access:
            raise AuthenticationFailed(
                "Dashboard access has been disabled."
            )

        if employee.employee_status != Employee.EmployeeStatus.ACTIVE:
            raise AuthenticationFailed(
                "Employee account is not active."
            )

        # ------------------------------------------------
        # JWT Tokens
        # ------------------------------------------------

        refresh = RefreshToken.for_user(user)

        access = refresh.access_token

        # ------------------------------------------------
        # Roles
        # ------------------------------------------------

        roles = list(
            employee.roles.values(
                "id",
                "role_name",
                "role_code",
            )
        )

        # ------------------------------------------------
        # Permissions
        # ------------------------------------------------

        permissions = PermissionService.group_by_module(employee)
        menus = MenuService.build(permissions, roles)
        permissions = MenuService.visible_permissions(permissions, menus)

        return {
            "refresh": str(refresh),
            "access": str(access),
            "user": user,
            "employee": employee,
            "roles": roles,
            "permissions": permissions,
            "menus": menus,
        }