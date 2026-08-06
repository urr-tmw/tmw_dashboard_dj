from django.contrib.auth import get_user_model
from django.db import transaction

from accounts.models import Employee

User = get_user_model()


class EmployeeCreateService:
    """
    Service responsible for onboarding a new employee.
    Creates User + Employee + Role assignment
    """

    @staticmethod
    @transaction.atomic
    def create_employee(validated_data):

        # -------------------------
        # Extract User Fields
        # -------------------------
        username = validated_data.pop("username")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        # -------------------------
        # Extract Roles
        # -------------------------
        roles = validated_data.pop("roles", [])
        print("Roles:", roles)
        
        # -------------------------
        # Create User
        # -------------------------
        user = User(
            username=username,
            email=email,
            is_active=True,
        )

        user.set_password(password)
        user.save()

        # -------------------------
        # Create Employee
        # -------------------------
        employee = Employee.objects.create(
            user=user,
            **validated_data,
        )

        # -------------------------
        # Assign Roles
        # -------------------------
        if roles:
            employee.roles.set(roles)

        return employee