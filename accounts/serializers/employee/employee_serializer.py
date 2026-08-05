from rest_framework import serializers
from accounts.models import Employee
from django.contrib.auth import get_user_model

from accounts.serializers.role.role_serializer import RoleSerializer

User = get_user_model()

class EmployeeSerializer(serializers.ModelSerializer):

    
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    user_email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )
    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )
    department_name = serializers.CharField(
        source="department.dept_name",
        read_only=True,
    )

    designation_name = serializers.CharField(
        source="designation.designation_name",
        read_only=True,
    )
    
    reporting_manager_name = serializers.SerializerMethodField()
    roles = RoleSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Employee
        fields = (
            "id",
            "user",
            "user_email",
            "username",
            "roles",
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
            "user_email",
            "username",
        )

    def get_reporting_manager_name(self, obj):
        if obj.reporting_manager:
            return obj.reporting_manager.user.get_full_name()
        return None



