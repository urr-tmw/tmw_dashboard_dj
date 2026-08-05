from rest_framework import serializers

from accounts.models import Permission


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"
        read_only_fields = (
            "id",
            "permission_name",
            "permission_code",
            "created_at",
            "updated_at",
        )