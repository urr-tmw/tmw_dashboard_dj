

from django.urls import path

from accounts.views.designation.designation_view import DesignationAPIView, DesignationChoicesByDepartmentAPIView
from accounts.views.designation.designation_status_view import DesignationStatusAPIView


urlpatterns = [
    path(
        "choices/",
        DesignationChoicesByDepartmentAPIView.as_view(),
        name="designation-choices-by-department",
    ),
    path(
        "",
        DesignationAPIView.as_view(),
        name="designation-list-create",
    ),
    path(
        "<int:designation_id>/",
        DesignationAPIView.as_view(),
        name="designation-detail",
    ),
    path(
        "<int:designation_id>/status/",
        DesignationStatusAPIView.as_view(),
        name="designation-status",
    ),
]