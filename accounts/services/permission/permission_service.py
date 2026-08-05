from accounts.models import Permission
from accounts.serializers.permission.permission_serializer import PermissionSerializer

from common.base_service import BaseMasterService


class PermissionService(BaseMasterService):

    model = Permission
    serializer_class = PermissionSerializer
    lookup_field = "permission_id"