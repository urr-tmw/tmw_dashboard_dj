from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from accounts.serializers.auth.login_serializer import LoginSerializer
from accounts.services.auth.login_service import LoginService

from common.constants import LOGIN_SUCCESSFUL

from utils.unified_response import api_response
from utils.decorators import validate_required_keys


class LoginAPIView(APIView):
    """
    Dashboard Login API
    """

    permission_classes = [AllowAny]
    @validate_required_keys(
    required_keys=["login", "password"],
    source="data"
)
    def post(self, request):
        """
        Login using Username/Email + Password
        """

        serializer = LoginSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        login_data = LoginService.login(
            serializer.validated_data,
        )

        user = login_data["user"]
        employee = login_data["employee"]

        response = {
            "access": login_data["access"],
            "refresh": login_data["refresh"],
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_superuser": user.is_superuser,
                "is_staff": user.is_staff,
            },
            "employee": None,
            "roles": login_data["roles"],
            "permissions": login_data["permissions"],
        }

        if employee:
            response["employee"] = {
                "id": employee.id,
                "employee_code": employee.employee_code,
                "department": employee.department.dept_name,
                "designation": employee.designation.designation_name,
                "dashboard_access": employee.dashboard_access,
                "employee_status": employee.employee_status,
            }

        return api_response(
            success=True,
            message=LOGIN_SUCCESSFUL,
            data=response,
            http_status=status.HTTP_200_OK,
        )