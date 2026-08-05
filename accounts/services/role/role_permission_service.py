from django.shortcuts import get_object_or_404
from django.db import transaction

from accounts.models import Role, Permission


class RolePermissionService:

    @staticmethod
    def get_role(role_id):

        return get_object_or_404(
            Role,
            id=role_id,
        )

    @staticmethod
    @transaction.atomic
    def assign_permissions(role_id, permission_ids):

        role = RolePermissionService.get_role(role_id)

        permissions = Permission.objects.filter(
            id__in=permission_ids
        )

        role.permissions.add(*permissions)

        return role

    @staticmethod
    @transaction.atomic
    def remove_permissions(role_id, permission_ids):

        role = RolePermissionService.get_role(role_id)

        permissions = Permission.objects.filter(
            id__in=permission_ids
        )

        role.permissions.remove(*permissions)

        return role

    @staticmethod
    @transaction.atomic
    def replace_permissions(role_id, permission_ids):

        role = RolePermissionService.get_role(role_id)

        permissions = Permission.objects.filter(
            id__in=permission_ids
        )

        role.permissions.set(permissions)

        return role

    @staticmethod
    def get_permissions(role_id):

        role = RolePermissionService.get_role(role_id)

        return role.permissions.all()