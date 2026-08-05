from rest_framework import serializers

from accounts.models import Permission


class RolePermissionSerializer(serializers.Serializer):
    """
    Serializer for assigning/removing permissions from a role.
    """

    permission_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
    )

    def validate_permission_ids(self, value):

        permissions = Permission.objects.filter(id__in=value)

        if permissions.count() != len(set(value)):
            raise serializers.ValidationError(
                "One or more permission IDs are invalid."
            )

        return value