from rest_framework import status
from rest_framework.views import APIView

from accounts.serializers.permission.permission_serializer import PermissionSerializer
from accounts.services.permission.permission_service import PermissionService

from common.constants import (
    CREATED_SUCCESSFULLY,
    UPDATED_SUCCESSFULLY,
    FETCHED_SUCCESSFULLY,
    LIST_FETCHED_SUCCESSFULLY,
    PERMISSION,
)

from utils.unified_response import api_response
from accounts.permissions.dashboard_permission import DashboardPermission


class PermissionAPIView(APIView):
    """
    Permission CRUD APIs
    """

    permission_classes = [DashboardPermission]

    def get(self, request, permission_id=None):
        """
        List all permissions or retrieve single permission.
        """

        if permission_id:
            permission = PermissionService.get_by_id(permission_id)
            serializer = PermissionSerializer(permission)

            return api_response(
                success=True,
                message=FETCHED_SUCCESSFULLY.format(PERMISSION),
                data=serializer.data,
                http_status=status.HTTP_200_OK,
            )

        permissions = PermissionService.get_queryset()
        serializer = PermissionSerializer(permissions, many=True)

        return api_response(
            success=True,
            message=LIST_FETCHED_SUCCESSFULLY.format(PERMISSION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def post(self, request):
        """
        Create Permission
        """

        permission = PermissionService.create(request.data)
        serializer = PermissionSerializer(permission)

        return api_response(
            success=True,
            message=CREATED_SUCCESSFULLY.format(PERMISSION),
            data=serializer.data,
            http_status=status.HTTP_201_CREATED,
        )

    def put(self, request, permission_id):
        """
        Update Permission
        """

        permission = PermissionService.update(
            permission_id,
            request.data,
        )

        serializer = PermissionSerializer(permission)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(PERMISSION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def patch(self, request, permission_id):
        """
        Partial Update Permission
        """

        permission = PermissionService.partial_update(
            permission_id,
            request.data,
        )

        serializer = PermissionSerializer(permission)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(PERMISSION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def delete(self, request, permission_id):
        """
        Delete Permission
        """

        PermissionService.delete(permission_id)

        return api_response(
            success=True,
            message=f"{PERMISSION} deleted successfully.",
            http_status=status.HTTP_204_NO_CONTENT,
        )