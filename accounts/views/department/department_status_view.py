from rest_framework import status
from rest_framework.views import APIView

from accounts.serializers.department.department_serializer import DepartmentSerializer
from accounts.services.department.department_service import DepartmentService

from common.constants import (
    STATUS_UPDATED_SUCCESSFULLY,
    DEPARTMENT,
)

from utils.unified_response import api_response
from rest_framework.permissions import AllowAny
from accounts.permissions.dashboard_permission import DashboardPermission
class DepartmentStatusAPIView(APIView):
    permission_classes = [DashboardPermission]
    """
    Activate / Deactivate Department
    """

    def patch(self, request, department_id):
        print("request.data", request.data)
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