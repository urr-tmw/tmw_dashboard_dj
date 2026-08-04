from rest_framework import serializers
from accounts.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    department_name = serializers.CharField(
        source="department.dept_name",
        read_only=True,
    )

    designation_name = serializers.CharField(
        source="designation.designation_name",
        read_only=True,
    )

    reporting_manager_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            "id",
            "user",
            "employee_code",
            "department",
            "department_name",
            "designation",
            "designation_name",
            "reporting_manager",
            "reporting_manager_name",
            "joining_date",
            "dashboard_access",
            "employee_status",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "department_name",
            "designation_name",
            "reporting_manager_name",
        )

    def get_reporting_manager_name(self, obj):
        if obj.reporting_manager:
            return obj.reporting_manager.user.get_full_name()
        return None