from rest_framework import status
from rest_framework.views import APIView

from accounts.serializers.department.department_serializer import DepartmentSerializer
from accounts.services.department.department_service import DepartmentService

from common.constants import (
    CREATED_SUCCESSFULLY,
    UPDATED_SUCCESSFULLY,
    FETCHED_SUCCESSFULLY,
    LIST_FETCHED_SUCCESSFULLY,
    DEPARTMENT,
)

from utils.unified_response import api_response
from accounts.permissions.dashboard_permission import DashboardPermission
from rest_framework.permissions import AllowAny
class DepartmentAPIView(APIView):
    """
    Department CRUD APIs
    """
    permission_classes = [DashboardPermission]
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