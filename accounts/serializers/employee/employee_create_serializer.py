from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import (
    Employee,
    Department,
    Designation,
    Role,
)
User = get_user_model()


class EmployeeCreateSerializer(serializers.Serializer):

    # User Information
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # Employee Information
    employee_code = serializers.CharField(max_length=20)

    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )

    designation = serializers.PrimaryKeyRelatedField(
        queryset=Designation.objects.all()
    )

    reporting_manager = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        required=False,
        allow_null=True,
    )

    joining_date = serializers.DateField()

    dashboard_access = serializers.BooleanField(default=True)

    employee_status = serializers.ChoiceField(
        choices=Employee.EmployeeStatus.choices
    )

    roles = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        many=True,
        required=False,
    )

    def validate_username(self, value):

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Username already exists."
            )

        return value

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value

    def validate_employee_code(self, value):

        if Employee.objects.filter(employee_code=value).exists():
            raise serializers.ValidationError(
                "Employee code already exists."
            )

        return value