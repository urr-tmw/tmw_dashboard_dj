# accounts/views/department/department_status_view.py

from rest_framework import status
from rest_framework.views import APIView

from accounts.serializers.department.department_serializer import DepartmentSerializer
from accounts.services.department.department_service import DepartmentService

from common.constants import (
    STATUS_UPDATED_SUCCESSFULLY,
    DEPARTMENT,
)
from common.permissions import DepartmentPermission
from utils.unified_response import api_response
from accounts.permissions.dashboard_permission import DashboardPermission


class DepartmentStatusAPIView(APIView):
    """
    Activate / Deactivate Department

    PATCH is treated as an update action.
    """

    permission_classes = [DashboardPermission]

    permission_map = {
        "PATCH": DepartmentPermission.UPDATE,
    }

    def patch(self, request, department_id):
        department = DepartmentService.update_status(
            object_id=department_id,
            is_active=request.data.get("is_active"),
        )

        serializer = DepartmentSerializer(department)

        return api_response(
            success=True,
            message=STATUS_UPDATED_SUCCESSFULLY.format(DEPARTMENT),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )