from django.db import transaction
from django.shortcuts import get_object_or_404

from accounts.models import Employee, Role


class EmployeeRoleService:

    @staticmethod
    def get_employee(employee_id):
        return get_object_or_404(
            Employee,
            id=employee_id,
        )

    @staticmethod
    @transaction.atomic
    def assign_roles(employee_id, role_ids):

        employee = EmployeeRoleService.get_employee(employee_id)

        roles = Role.objects.filter(id__in=role_ids)

        employee.roles.add(*roles)

        return employee

    @staticmethod
    @transaction.atomic
    def remove_roles(employee_id, role_ids):

        employee = EmployeeRoleService.get_employee(employee_id)

        roles = Role.objects.filter(id__in=role_ids)

        employee.roles.remove(*roles)

        return employee

    @staticmethod
    @transaction.atomic
    def replace_roles(employee_id, role_ids):

        employee = EmployeeRoleService.get_employee(employee_id)

        roles = Role.objects.filter(id__in=role_ids)

        employee.roles.set(roles)

        return employee

    @staticmethod
    def get_roles(employee_id):

        employee = EmployeeRoleService.get_employee(employee_id)

        return employee.roles.all()