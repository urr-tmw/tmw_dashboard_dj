# dashboard_permission.py

from rest_framework.permissions import AllowAny

class DashboardPermission(AllowAny):
    """
    Temporary permission during development.
    """
    pass