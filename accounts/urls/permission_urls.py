from django.urls import path

from accounts.views.permission.permission_view import PermissionAPIView

urlpatterns = [
    path(
        "",
        PermissionAPIView.as_view(),
        name="permission-list-create",
    ),
    path(
        "<int:permission_id>/",
        PermissionAPIView.as_view(),
        name="permission-detail",
    ),
    
]