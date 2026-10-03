"""
Sidebar catalog.

Main  -> group on a sub menu          (Administration)
Sub   -> one sidebar link             (Users & Roles)
Child -> one tab under that link      (Employees, Department, ...)

PUBLIC_MENUS are shown to every role.
ROLE_MENUS adds extra main menus for specific roles.
Permissions then decide which tabs appear under a link that has tabs.
"""

from common.permissions import (
    DepartmentPermission,
    DesignationPermission,
    EmployeePermission,
    PermissionConstant,
    RolePermission,
)


# Main section is `group`. Each row is one sidebar link.
SUB_MENUS = [
    #Workspace
    {   
        "code": "self_storage",
        "label": "Self Storage",
        "icon": "self_storage",
        "url": "/self-storage",
        "group": "Workspace",

    },
    {
        "code": "resident_delivery",
        "label": "Resident Delivery",
        "icon": "resident_delivery",
        "url": "/resident-delivery",
        "group": "Workspace",
    },
    {
        "code": "assistant_delivery",
        "label": "Assistant Delivery",
        "icon": "assistant_delivery",
        "url": "/assistant-delivery",
        "group": "Workspace",
    },
    # Administration
    {
        "code": "users-roles",
        "label": "Users & Roles",
        "icon": "users",
        "url": "/users-roles",
        "group": "Administration",
    },
    {
        "code": "billing",
        "label": "Billing",
        "icon": "billing",
        "url": "/billing",
        "group": "Administration",
    },
    {
        "code": "support",
        "label": "Support",
        "icon": "support",
        "url": "/support",
        "group": "Administration",
    },
    {
        "code": "audit",
        "label": "Audit",
        "icon": "audit",
        "url": "/audit",
        "group": "Administration",
    },
    #Operations
    {
        "code": "reports",
        "label": "Reports",
        "icon": "reports",
        "url": "/reports",
        "group": "Operations",
    },
    {
        "code": "monitoring",
        "label": "Monitoring",
        "icon": "monitoring",
        "url": "/monitoring",
        "group": "Operations",
    },
    {
        "code": "notifications",        
        "label": "Notifications",
        "icon": "notifications",
        "url": "/notifications",
        "group": "Operations",
    },
    #Employee
    {
        "code": "employees",
        "label": "Employees",
        "icon": "employee",
        "url": "/employees",
        "group": "Employee Management",
    },
    #Settings
    {
        "code": "settings",
        "label": "Settings",
        "icon": "settings",
        "url": "/settings",
        "group": "Settings",
    },
    {
        "code": "user_manual",
        "label": "User Manual",
        "icon": "user_manual",
        "url": "/user-manual",
        "group": "Settings",
        
    }
]



# Tabs under a sub. `menu` is the sub code above.
MENU_ITEMS = [
    {
        "code": "employees",
        "label": "Employees",
        "url": "/employees",
        "menu": "users-roles",
        "permission": EmployeePermission.VIEW,
    },
    {
        "code": "departments",
        "label": "Department",
        "url": "/departments",
        "menu": "users-roles",
        "permission": DepartmentPermission.VIEW,
    },
    {
        "code": "designations",
        "label": "Designation",
        "url": "/designations",
        "menu": "users-roles",
        "permission": DesignationPermission.VIEW,
    },
    {
        "code": "roles",
        "label": "Roles",
        "url": "/roles",
        "menu": "users-roles",
        "permission": RolePermission.VIEW,
    },
    {
        "code": "permissions",
        "label": "Permissions",
        "url": "/permissions",
        "menu": "users-roles",
        "permission": PermissionConstant.VIEW,
    },
]


# Main menus every role can see.
# Add a group name here when a new menu should be visible to all roles.
PUBLIC_MENUS = [
    "Operations",
]


# role_code -> extra main menus that role can open.
# Administration stays limited to these roles.
ROLE_MENUS = {
    "HR_MANAGER": ["Administration"],
    "SUPER_ADMIN": ["Administration"],
    "SYSTEM_ADMIN": ["Administration"],
    "ADMIN": ["Administration"],
    "DEPARTMENT_MANAGER": ["Administration"],
    # "OPERATIONS": ["Administration"]
}
