from django.db import transaction
from django.shortcuts import get_object_or_404

from accounts.models import Department
from accounts.serializers.department.department_serializer import DepartmentSerializer


class DepartmentService:

    @staticmethod
    def get_all_departments():
        """
        Returns all departments ordered by name.
        """
        return Department.objects.all().order_by("dept_name")

    @staticmethod
    def get_department_by_id(department_id):
        """
        Returns a single department object.
        """
        return get_object_or_404(Department, id=department_id)

    @staticmethod
    @transaction.atomic
    def create_department(data):
        """
        Create a new department.
        """

        serializer = DepartmentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.instance

    @staticmethod
    @transaction.atomic
    def update_department(department_id, data):
        """
        Update an existing department.
        """

        department = DepartmentService.get_department_by_id(department_id)

        serializer = DepartmentSerializer(
            department,
            data=data,
            partial=False
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.instance

    @staticmethod
    @transaction.atomic
    def change_department_status(department_id, is_active):
        """
        Activate / Deactivate department.
        """

        department = DepartmentService.get_department_by_id(department_id)

        department.is_active = is_active
        department.save(update_fields=["is_active"])

        return department
