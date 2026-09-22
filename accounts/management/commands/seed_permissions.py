from django.core.management.base import BaseCommand
from django.db import transaction

from accounts.models import Permission, Role


# ============================================================
# All permission definitions
# Each tuple: (module, action, permission_name, permission_code)
# ============================================================

PERMISSIONS = [

    # Department
    ("Department", "view",   "Department View",   "department.view"),
    ("Department", "create", "Department Create", "department.create"),
    ("Department", "update", "Department Update", "department.update"),
    ("Department", "delete", "Department Delete", "department.delete"),
    ("Department", "admin",  "Department Admin",  "department.admin"),

    # Designation
    ("Designation", "view",   "Designation View",   "designation.view"),
    ("Designation", "create", "Designation Create", "designation.create"),
    ("Designation", "update", "Designation Update", "designation.update"),
    ("Designation", "delete", "Designation Delete", "designation.delete"),
    ("Designation", "admin",  "Designation Admin",  "designation.admin"),

    # Employee
    ("Employee", "view",   "Employee View",   "employee.view"),
    ("Employee", "create", "Employee Create", "employee.create"),
    ("Employee", "update", "Employee Update", "employee.update"),
    ("Employee", "delete", "Employee Delete", "employee.delete"),
    ("Employee", "admin",  "Employee Admin",  "employee.admin"),

    # Role
    ("Role", "view",   "Role View",   "role.view"),
    ("Role", "create", "Role Create", "role.create"),
    ("Role", "update", "Role Update", "role.update"),
    ("Role", "delete", "Role Delete", "role.delete"),
    ("Role", "admin",  "Role Admin",  "role.admin"),

    # Permission
    ("Permission", "view",   "Permission View",   "permission.view"),
    ("Permission", "create", "Permission Create", "permission.create"),
    ("Permission", "update", "Permission Update", "permission.update"),
    ("Permission", "delete", "Permission Delete", "permission.delete"),
    ("Permission", "admin",  "Permission Admin",  "permission.admin"),

]


# ============================================================
# Role definitions
# Each dict: role_name, role_code, description, permission_codes
# ============================================================

ROLES = [
    {
        "role_name": "Super Admin",
        "role_code": "SUPER_ADMIN",
        "description": "Full access to all modules.",
        "permission_codes": [p[3] for p in PERMISSIONS],  # all permissions
    },
    {
        "role_name": "HR Manager",
        "role_code": "HR_MANAGER",
        "description": "Manages employees, departments, and designations.",
        "permission_codes": [
            "department.view",
            "designation.view",
            "employee.view",
            "employee.create",
            "employee.update",
        ],
    },
    {
        "role_name": "Department Manager",
        "role_code": "DEPARTMENT_MANAGER",
        "description": "Can view and update departments and designations.",
        "permission_codes": [
            "department.view",
            "department.update",
            "designation.view",
            "employee.view",
        ],
    },
    {
        "role_name": "Viewer",
        "role_code": "VIEWER",
        "description": "Read-only access to all modules.",
        "permission_codes": [
            "department.view",
            "designation.view",
            "employee.view",
            "role.view",
            "permission.view",
        ],
    },
]


class Command(BaseCommand):
    help = "Seeds Permissions and Roles into the database."

    def handle(self, *args, **options):
        self.stdout.write("\n" + "=" * 50)
        self.stdout.write("  Seeding Permissions and Roles")
        self.stdout.write("=" * 50 + "\n")

        with transaction.atomic():
            self._seed_permissions()
            self._seed_roles()

        self.stdout.write("\n" + self.style.SUCCESS("✅  Seed complete.\n"))

    # ----------------------------------------------------------

    def _seed_permissions(self):
        self.stdout.write(self.style.HTTP_INFO("\n📋  Permissions"))
        self.stdout.write("-" * 40)

        created_count = 0
        skipped_count = 0

        for module, action, permission_name, permission_code in PERMISSIONS:

            permission, created = Permission.objects.get_or_create(
                permission_code=permission_code,
                defaults={
                    "module": module,
                    "action": action,
                    "permission_name": permission_name,
                    "is_active": True,
                },
            )

            if created:
                self.stdout.write(f"  ✅  Created : {permission_code}")
                created_count += 1
            else:
                self.stdout.write(f"  ⏭️   Exists  : {permission_code}")
                skipped_count += 1

        self.stdout.write(
            f"\n  Created: {created_count}  |  Already existed: {skipped_count}"
        )

    # ----------------------------------------------------------

    def _seed_roles(self):
        self.stdout.write(self.style.HTTP_INFO("\n🎭  Roles"))
        self.stdout.write("-" * 40)

        for role_data in ROLES:

            role, created = Role.objects.get_or_create(
                role_code=role_data["role_code"],
                defaults={
                    "role_name": role_data["role_name"],
                    "description": role_data["description"],
                    "is_active": True,
                },
            )

            # Assign permissions
            permissions = Permission.objects.filter(
                permission_code__in=role_data["permission_codes"],
            )
            role.permissions.set(permissions)

            status = "Created" if created else "Updated"
            self.stdout.write(
                f"  ✅  {status} : {role.role_name} ({permissions.count()} permissions)"
            )
