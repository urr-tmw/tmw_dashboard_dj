from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from accounts.permissions.dashboard_permission import DashboardPermission
from utils.unified_response import api_response

from accounts.services.designation.designation_service import DesignationService
from accounts.serializers.designation.designation_serializer import DesignationSerializer

from common.constants import (
    DESIGNATION,
    CREATED_SUCCESSFULLY,
    UPDATED_SUCCESSFULLY,
    RETRIEVED_SUCCESSFULLY,
    DELETED_SUCCESSFULLY,
    STATUS_UPDATED_SUCCESSFULLY,
)



class DesignationAPIView(APIView):

    permission_classes = [DashboardPermission]

    def get(self, request, designation_id=None):

        if designation_id:

            designation = DesignationService.get_by_id(
                designation_id
            )

            serializer = DesignationSerializer(designation)

            return api_response(
                success=True,
                message=RETRIEVED_SUCCESSFULLY.format(DESIGNATION),
                data=serializer.data,
                http_status=status.HTTP_200_OK,
            )

        designations = DesignationService.get_queryset()

        serializer = DesignationSerializer(
            designations,
            many=True,
        )

        return api_response(
            success=True,
            message=RETRIEVED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def post(self, request):

        designation = DesignationService.create(
            request.data
        )

        serializer = DesignationSerializer(designation)

        return api_response(
            success=True,
            message=CREATED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_201_CREATED,
        )

    def put(self, request, designation_id):

        designation = DesignationService.update(
            designation_id,
            request.data,
        )

        serializer = DesignationSerializer(designation)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def patch(self, request, designation_id):

        designation = DesignationService.partial_update(
            designation_id,
            request.data,
        )

        serializer = DesignationSerializer(designation)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )