from django.urls import path

from accounts.views.department.department_view import DepartmentAPIView
from accounts.views.department.department_status_view import DepartmentStatusAPIView

urlpatterns = [

    path(
        "",
        DepartmentAPIView.as_view(),
        name="department-list-create",
    ),

    path(
        "<int:department_id>/",
        DepartmentAPIView.as_view(),
        name="department-detail",
    ),

    path(
        "<int:department_id>/status/",
        DepartmentStatusAPIView.as_view(),
        name="department-status",
    ),
]