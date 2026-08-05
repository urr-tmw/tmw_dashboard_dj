from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from accounts.permissions.dashboard_permission import DashboardPermission
from rest_framework import status

from utils.unified_response import api_response

from accounts.services.designation.designation_service import DesignationService
from accounts.serializers.designation.designation_serializer import DesignationSerializer

from common.constants import (
    DESIGNATION,
    CREATED_SUCCESSFULLY,
    UPDATED_SUCCESSFULLY,
    RETRIEVED_SUCCESSFULLY,
    STATUS_UPDATED_SUCCESSFULLY,
)

class DesignationStatusAPIView(APIView):

    permission_classes = [AllowAny]

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