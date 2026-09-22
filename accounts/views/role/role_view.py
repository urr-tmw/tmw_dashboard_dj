# accounts/views/role/role_view.py

from rest_framework import status
from rest_framework.views import APIView

from accounts.serializers.role.role_serializer import RoleSerializer
from accounts.services.role.role_service import RoleService

from common.constants import (
    CREATED_SUCCESSFULLY,
    UPDATED_SUCCESSFULLY,
    FETCHED_SUCCESSFULLY,
    LIST_FETCHED_SUCCESSFULLY,
    ROLE,
)
from common.permissions import RolePermission
from utils.unified_response import api_response
from accounts.permissions.dashboard_permission import DashboardPermission


class RoleAPIView(APIView):
    """
    Role CRUD APIs

    Permissions enforced per HTTP method via RBAC permission_map.
    """

    permission_classes = [DashboardPermission]

    permission_map = {
        "GET":    RolePermission.VIEW,
        "POST":   RolePermission.CREATE,
        "PUT":    RolePermission.UPDATE,
        "PATCH":  RolePermission.UPDATE,
        "DELETE": RolePermission.DELETE,
    }

    def get(self, request, role_id=None):
        """
        List all roles or retrieve single role.
        """

        if role_id:
            role = RoleService.get_by_id(role_id)
            serializer = RoleSerializer(role)

            return api_response(
                success=True,
                message=FETCHED_SUCCESSFULLY.format(ROLE),
                data=serializer.data,
                http_status=status.HTTP_200_OK,
            )

        roles = RoleService.get_queryset()
        serializer = RoleSerializer(roles, many=True)

        return api_response(
            success=True,
            message=LIST_FETCHED_SUCCESSFULLY.format(ROLE),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def post(self, request):
        """
        Create Role
        """

        role = RoleService.create(request.data)
        serializer = RoleSerializer(role)

        return api_response(
            success=True,
            message=CREATED_SUCCESSFULLY.format(ROLE),
            data=serializer.data,
            http_status=status.HTTP_201_CREATED,
        )

    def put(self, request, role_id):
        """
        Update Role
        """

        role = RoleService.update(
            role_id,
            request.data,
        )

        serializer = RoleSerializer(role)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(ROLE),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def patch(self, request, role_id):
        """
        Partial Update Role
        """

        role = RoleService.partial_update(
            role_id,
            request.data,
        )

        serializer = RoleSerializer(role)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(ROLE),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )