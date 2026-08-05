from rest_framework import serializers

from accounts.models import Role


class EmployeeRoleSerializer(serializers.Serializer):
    """
    Serializer for assigning/removing roles from an employee.
    """

    role_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
    )

    def validate_role_ids(self, value):

        roles = Role.objects.filter(id__in=value)

        if roles.count() != len(set(value)):
            raise serializers.ValidationError(
                "One or more role IDs are invalid."
            )

        return value