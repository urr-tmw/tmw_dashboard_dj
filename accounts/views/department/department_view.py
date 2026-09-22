# accounts/views/department/department_view.py

from rest_framework import status
from rest_framework.views import APIView

from accounts.serializers.department.department_serializer import DepartmentSerializer
from accounts.services.department.department_service import DepartmentService
from utils.decorators import validate_required_keys
from common.constants import (
    CREATED_SUCCESSFULLY,
    UPDATED_SUCCESSFULLY,
    FETCHED_SUCCESSFULLY,
    LIST_FETCHED_SUCCESSFULLY,
    DEPARTMENT,
)
from common.permissions import DepartmentPermission
from utils.unified_response import api_response
from accounts.permissions.dashboard_permission import DashboardPermission


class DepartmentAPIView(APIView):
    """
    Department CRUD APIs

    Permissions enforced per HTTP method via RBAC permission_map.
    """

    permission_classes = [DashboardPermission]

    permission_map = {
        "GET":    DepartmentPermission.VIEW,
        "POST":   DepartmentPermission.CREATE,
        "PUT":    DepartmentPermission.UPDATE,
        "PATCH":  DepartmentPermission.UPDATE,
        "DELETE": DepartmentPermission.DELETE,
    }

    def get(self, request, department_id=None):
        """
        List all departments or retrieve a single department.
        """

        if department_id:
            department = DepartmentService.get_by_id(department_id)
            serializer = DepartmentSerializer(department)

            return api_response(
                success=True,
                message=FETCHED_SUCCESSFULLY.format(DEPARTMENT),
                data=serializer.data,
                http_status=status.HTTP_200_OK,
            )

        departments = DepartmentService.get_queryset()
        serializer = DepartmentSerializer(departments, many=True)

        return api_response(
            success=True,
            message=LIST_FETCHED_SUCCESSFULLY.format(DEPARTMENT),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    @validate_required_keys(
        required_keys=["dept_name", "dept_code"],
        source="data",
    )
    def post(self, request):
        """
        Create Department
        """

        department = DepartmentService.create(request.data)
        serializer = DepartmentSerializer(department)

        return api_response(
            success=True,
            message=CREATED_SUCCESSFULLY.format(DEPARTMENT),
            data=serializer.data,
            http_status=status.HTTP_201_CREATED,
        )

    def put(self, request, department_id):
        """
        Update Department
        """

        department = DepartmentService.update(
            department_id,
            request.data,
        )

        serializer = DepartmentSerializer(department)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(DEPARTMENT),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def patch(self, request, department_id):
        """
        Partial Update Department
        """

        department = DepartmentService.partial_update(
            department_id,
            request.data,
        )

        serializer = DepartmentSerializer(department)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(DEPARTMENT),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )