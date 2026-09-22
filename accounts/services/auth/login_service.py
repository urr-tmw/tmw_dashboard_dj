from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import Employee
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

            return {
                "refresh": str(refresh),
                "access": str(access),
                "user": user,
                "employee": None,
                "roles": [
                    {
                        "id": 0,
                        "role_name": SYSTEM_ADMIN_ROLE_NAME,
                        "role_code": SYSTEM_ADMIN_ROLE_CODE,
                    }
                ],
                "permissions": [SUPER_ADMIN_PERMISSION],
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

        permissions = list(
            employee.roles
            .prefetch_related("permissions")
            .values_list(
                "permissions__permission_code",
                flat=True,
            )
            .distinct()
        )

        return {
            "refresh": str(refresh),
            "access": str(access),
            "user": user,
            "employee": employee,
            "roles": roles,
            "permissions": permissions,
        }