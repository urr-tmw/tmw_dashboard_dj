from django.utils.text import slugify

from common.constants import SUPER_ADMIN_PERMISSION
from common.menus import MENU_ITEMS, PUBLIC_MENUS, ROLE_MENUS, SUB_MENUS
from common.permissions import (
    DepartmentPermission,
    DesignationPermission,
    EmployeePermission,
    PermissionConstant,
    RolePermission,
)


def _declared_codes():
    classes = (
        DepartmentPermission,
        DesignationPermission,
        EmployeePermission,
        RolePermission,
        PermissionConstant,
    )
    codes = []

    for permission_cls in classes:
        for name, value in vars(permission_cls).items():
            if name.isupper() and isinstance(value, str):
                codes.append(value)

    return codes


DECLARED_CODES = _declared_codes()


class MenuService:
    """
    Builds the sidebar from the static menu catalog.
    """

    @staticmethod
    def _codes_for_item(item, permissions, allow_all):
        prefix = item["permission"].split(".", 1)[0] + "."

        if allow_all:
            return [
                code
                for code in DECLARED_CODES
                if code.startswith(prefix)
            ]

        matched = []

        for codes in permissions.values():
            for code in codes:
                if code.startswith(prefix) and code not in matched:
                    matched.append(code)

        return matched

    @staticmethod
    def build(permissions, roles):
        granted = {
            code
            for codes in permissions.values()
            for code in codes
        }
        allow_all = SUPER_ADMIN_PERMISSION in granted

        allowed_groups = set(PUBLIC_MENUS)
        if not allow_all:
            for role in roles:
                allowed_groups.update(
                    ROLE_MENUS.get(role["role_code"], [])
                )

        children_by_menu = {}

        for item in MENU_ITEMS:
            if not allow_all and item["permission"] not in granted:
                continue

            children_by_menu.setdefault(item["menu"], []).append(
                {
                    "code": item["code"],
                    "label": item["label"],
                    "url": item["url"],
                    "permissions": MenuService._codes_for_item(
                        item,
                        permissions,
                        allow_all,
                    ),
                }
            )

        grouped = {}

        for sub in SUB_MENUS:
            if not allow_all and sub["group"] not in allowed_groups:
                continue

            children = children_by_menu.get(sub["code"], [])
            has_tabs = any(item["menu"] == sub["code"] for item in MENU_ITEMS)

            if has_tabs and not children:
                continue

            section = grouped.setdefault(
                sub["group"],
                {
                    "code": slugify(sub["group"]),
                    "label": sub["group"],
                    "subs": [],
                },
            )
            section["subs"].append(
                {
                    "code": sub["code"],
                    "label": sub["label"],
                    "icon": sub["icon"],
                    "url": sub["url"],
                    "children": children,
                }
            )

        return list(grouped.values())

    @staticmethod
    def visible_permissions(permissions, menus):
        """
        Keeps permission codes that appear on a menu the role can see.
        A hidden menu, such as Administration for Operations, drops its
        permissions from the response as well.
        """

        granted = {
            code
            for codes in permissions.values()
            for code in codes
        }
        if SUPER_ADMIN_PERMISSION in granted:
            return permissions

        visible = set()

        for section in menus:
            for sub in section.get("subs", []):
                for child in sub.get("children", []):
                    visible.update(child.get("permissions", []))

        limited = {}

        for module, codes in permissions.items():
            kept = [code for code in codes if code in visible]
            if kept:
                limited[module] = kept

        return limited
