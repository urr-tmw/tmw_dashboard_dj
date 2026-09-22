# accounts/views/employee/employee_role_view.py

from rest_framework import status
from rest_framework.views import APIView

from accounts.permissions.dashboard_permission import DashboardPermission
from accounts.serializers.employee.employee_role_serializer import (
    EmployeeRoleSerializer,
)
from accounts.serializers.role.role_serializer import RoleSerializer
from accounts.services.employee.employee_role_service import (
    EmployeeRoleService,
)
from common.permissions import EmployeePermission
from utils.unified_response import api_response


class EmployeeRoleAPIView(APIView):
    """
    Assign / Remove / Replace Employee Roles

    All role mutations require employee.update permission since
    they modify the employee's role assignments.
    """

    permission_classes = [DashboardPermission]

    permission_map = {
        "GET":    EmployeePermission.VIEW,
        "POST":   EmployeePermission.UPDATE,
        "PUT":    EmployeePermission.UPDATE,
        "DELETE": EmployeePermission.UPDATE,
    }

    def get(self, request, employee_id):

        roles = EmployeeRoleService.get_roles(employee_id)

        serializer = RoleSerializer(
            roles,
            many=True,
        )

        return api_response(
            success=True,
            message="Employee roles fetched successfully.",
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def post(self, request, employee_id):

        serializer = EmployeeRoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        EmployeeRoleService.assign_roles(
            employee_id,
            serializer.validated_data["role_ids"],
        )

        return api_response(
            success=True,
            message="Roles assigned successfully.",
            http_status=status.HTTP_200_OK,
        )

    def put(self, request, employee_id):

        serializer = EmployeeRoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        EmployeeRoleService.replace_roles(
            employee_id,
            serializer.validated_data["role_ids"],
        )

        return api_response(
            success=True,
            message="Roles updated successfully.",
            http_status=status.HTTP_200_OK,
        )

    def delete(self, request, employee_id):

        serializer = EmployeeRoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        EmployeeRoleService.remove_roles(
            employee_id,
            serializer.validated_data["role_ids"],
        )

        return api_response(
            success=True,
            message="Roles removed successfully.",
            http_status=status.HTTP_200_OK,
        )