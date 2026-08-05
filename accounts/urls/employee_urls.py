from django.urls import path

from accounts.views.employee.employee_view import EmployeeAPIView
from accounts.views.employee.employee_role_view import EmployeeRoleAPIView

urlpatterns = [
    path(
        "",
        EmployeeAPIView.as_view(),
        name="employee-list-create",
    ),
    path(
        "<int:employee_id>/",
        EmployeeAPIView.as_view(),
        name="employee-detail",
    ),
    path(
        "<int:employee_id>/roles/",
        EmployeeRoleAPIView.as_view(),
        name="employee-roles",
    ),
]