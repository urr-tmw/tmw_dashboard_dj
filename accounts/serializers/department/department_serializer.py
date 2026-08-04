from rest_framework import serializers
from accounts.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "id",
            "dept_name",
            "dept_code",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

    def validate_dept_name(self, value):
        if Department.objects.filter(dept_name__iexact=value).exists():
            raise serializers.ValidationError(
                "Department name already exists."
            )
        return value.strip()

    def validate_dept_code(self, value):
        if Department.objects.filter(dept_code__iexact=value).exists():
            raise serializers.ValidationError(
                "Department code already exists."
            )
        return value.strip().upper()