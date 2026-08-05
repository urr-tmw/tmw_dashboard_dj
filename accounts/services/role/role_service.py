from accounts.models import Role
from accounts.serializers.role.role_serializer import RoleSerializer

from common.base_service import BaseMasterService


class RoleService(BaseMasterService):

    model = Role

    serializer_class = RoleSerializer

    ordering_field = "role_name"