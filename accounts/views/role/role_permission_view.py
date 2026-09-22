# accounts/views/role/role_permission_view.py

from rest_framework import status
from rest_framework.views import APIView

from accounts.permissions.dashboard_permission import DashboardPermission
from accounts.serializers.permission.permission_serializer import (
    PermissionSerializer,
)
from accounts.serializers.role.role_permission_serializer import (
    RolePermissionSerializer,
)
from accounts.services.role.role_permission_service import (
    RolePermissionService,
)
from common.permissions import RolePermission
from utils.unified_response import api_response


class RolePermissionAPIView(APIView):
    """
    Assign / Remove / Replace Role Permissions

    All operations require role.update permission since they
    mutate the role's permission set.
    """

    permission_classes = [DashboardPermission]

    permission_map = {
        "GET":    RolePermission.VIEW,
        "POST":   RolePermission.UPDATE,
        "PUT":    RolePermission.UPDATE,
        "DELETE": RolePermission.UPDATE,
    }

    def get(self, request, role_id):

        permissions = RolePermissionService.get_permissions(role_id)

        serializer = PermissionSerializer(
            permissions,
            many=True,
        )

        return api_response(
            success=True,
            message="Role permissions fetched successfully.",
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def post(self, request, role_id):

        serializer = RolePermissionSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        RolePermissionService.assign_permissions(
            role_id,
            serializer.validated_data["permission_ids"],
        )

        return api_response(
            success=True,
            message="Permissions assigned successfully.",
            http_status=status.HTTP_200_OK,
        )

    def delete(self, request, role_id):

        serializer = RolePermissionSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        RolePermissionService.remove_permissions(
            role_id,
            serializer.validated_data["permission_ids"],
        )

        return api_response(
            success=True,
            message="Permissions removed successfully.",
            http_status=status.HTTP_200_OK,
        )

    def put(self, request, role_id):

        serializer = RolePermissionSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        RolePermissionService.replace_permissions(
            role_id,
            serializer.validated_data["permission_ids"],
        )

        return api_response(
            success=True,
            message="Permissions updated successfully.",
            http_status=status.HTTP_200_OK,
        )