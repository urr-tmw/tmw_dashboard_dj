from django.urls import path

from accounts.views.role.role_permission_view import RolePermissionAPIView
from accounts.views.role.role_view import RoleAPIView

urlpatterns = [
    path(
        "",
        RoleAPIView.as_view(),
        name="role-list-create",
    ),
    path(
        "<int:role_id>/",
        RoleAPIView.as_view(),
        name="role-detail",
    ),
    path(
    "<int:role_id>/permissions/",
    RolePermissionAPIView.as_view(),
    name="role-permissions",
),
]