# accounts/views/designation/designation_status_view.py

from rest_framework.views import APIView
from rest_framework import status

from accounts.permissions.dashboard_permission import DashboardPermission
from utils.unified_response import api_response

from accounts.services.designation.designation_service import DesignationService
from accounts.serializers.designation.designation_serializer import DesignationSerializer

from common.constants import (
    DESIGNATION,
    STATUS_UPDATED_SUCCESSFULLY,
)
from common.permissions import DesignationPermission


class DesignationStatusAPIView(APIView):
    """
    Activate / Deactivate Designation

    PATCH is treated as an update action.
    """

    permission_classes = [DashboardPermission]

    permission_map = {
        "PATCH": DesignationPermission.UPDATE,
    }

    def patch(self, request, designation_id):

        designation = DesignationService.update_status(
            object_id=designation_id,
            is_active=request.data.get("is_active"),
        )

        serializer = DesignationSerializer(designation)

        return api_response(
            success=True,
            message=STATUS_UPDATED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )