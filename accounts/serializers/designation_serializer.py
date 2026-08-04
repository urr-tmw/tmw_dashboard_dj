from rest_framework import serializers
from accounts.models import Designation


class DesignationSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(
        source="department.dept_name",
        read_only=True,
    )

    class Meta:
        model = Designation
        fields = (
            "id",
            "department",
            "department_name",
            "designation_name",
            "designation_code",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "department_name",
        )

    def validate_designation_name(self, value):
        return value.strip()

    def validate_designation_code(self, value):
        return value.strip().upper()