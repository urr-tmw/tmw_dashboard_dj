# common/permissions.py
"""
Centralized RBAC permission string constants.

Usage:
    from common.permissions import DepartmentPermission
    required_permission = DepartmentPermission.VIEW
"""


# ==========================
# Department
# ==========================

class DepartmentPermission:
    VIEW   = "department.view"
    CREATE = "department.create"
    UPDATE = "department.update"
    DELETE = "department.delete"
    ADMIN  = "department.admin"


# ==========================
# Designation
# ==========================

class DesignationPermission:
    VIEW   = "designation.view"
    CREATE = "designation.create"
    UPDATE = "designation.update"
    DELETE = "designation.delete"
    ADMIN  = "designation.admin"


# ==========================
# Employee
# ==========================

class EmployeePermission:
    VIEW   = "employee.view"
    CREATE = "employee.create"
    UPDATE = "employee.update"
    DELETE = "employee.delete"
    ADMIN  = "employee.admin"


# ==========================
# Role
# ==========================

class RolePermission:
    VIEW   = "role.view"
    CREATE = "role.create"
    UPDATE = "role.update"
    DELETE = "role.delete"
    ADMIN  = "role.admin"


# ==========================
# Permission
# ==========================

class PermissionConstant:
    VIEW   = "permission.view"
    CREATE = "permission.create"
    UPDATE = "permission.update"
    DELETE = "permission.delete"
    ADMIN  = "permission.admin"