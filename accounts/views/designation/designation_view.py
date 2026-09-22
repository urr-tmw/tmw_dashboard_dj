# accounts/views/designation/designation_view.py

from rest_framework.views import APIView
from rest_framework import status

from accounts.permissions.dashboard_permission import DashboardPermission
from utils.unified_response import api_response

from accounts.models import Designation
from accounts.services.designation.designation_service import DesignationService
from accounts.serializers.designation.designation_serializer import DesignationSerializer

from common.constants import (
    DESIGNATION,
    CREATED_SUCCESSFULLY,
    UPDATED_SUCCESSFULLY,
    RETRIEVED_SUCCESSFULLY,
)
from common.permissions import DesignationPermission


class DesignationAPIView(APIView):
    """
    Designation CRUD APIs

    Permissions enforced per HTTP method via RBAC permission_map.
    """

    permission_classes = [DashboardPermission]

    permission_map = {
        "GET":    DesignationPermission.VIEW,
        "POST":   DesignationPermission.CREATE,
        "PUT":    DesignationPermission.UPDATE,
        "PATCH":  DesignationPermission.UPDATE,
        "DELETE": DesignationPermission.DELETE,
    }

    def get(self, request, designation_id=None):

        if designation_id:

            designation = DesignationService.get_by_id(
                designation_id
            )

            serializer = DesignationSerializer(designation)

            return api_response(
                success=True,
                message=RETRIEVED_SUCCESSFULLY.format(DESIGNATION),
                data=serializer.data,
                http_status=status.HTTP_200_OK,
            )

        designations = DesignationService.get_queryset()

        serializer = DesignationSerializer(
            designations,
            many=True,
        )

        return api_response(
            success=True,
            message=RETRIEVED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def post(self, request):

        designation = DesignationService.create(
            request.data
        )

        serializer = DesignationSerializer(designation)

        return api_response(
            success=True,
            message=CREATED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_201_CREATED,
        )

    def put(self, request, designation_id):

        designation = DesignationService.update(
            designation_id,
            request.data,
        )

        serializer = DesignationSerializer(designation)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def patch(self, request, designation_id):

        designation = DesignationService.partial_update(
            designation_id,
            request.data,
        )

        serializer = DesignationSerializer(designation)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )


class DesignationChoicesByDepartmentAPIView(APIView):
    """
    Returns designation choices filtered by one or more selected departments.

    Designed for frontend multi-select dropdowns where the user first picks
    their joined department(s) and then sees only the relevant designations.

    Usage:
        GET /api/designations/choices/?department_id=1
        GET /api/designations/choices/?department_id=1&department_id=2&department_id=3

    Query Params:
        department_id (int, repeatable) — IDs of the selected/joined departments.

    Response:
        List of designation objects filtered to those departments,
        ordered by department name then designation name.
    """

    permission_classes = [DashboardPermission]

    permission_map = {
        "GET": DesignationPermission.VIEW,
    }

    def get(self, request):

        # Collect all ?department_id= values (supports multi-select)
        department_ids = request.query_params.getlist("department_id")

        if not department_ids:
            return api_response(
                success=False,
                message="At least one 'department_id' query parameter is required.",
                data=[],
                http_status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate that all provided values are valid integers
        try:
            department_ids = [int(did) for did in department_ids]
        except ValueError:
            return api_response(
                success=False,
                message="All 'department_id' values must be valid integers.",
                data=[],
                http_status=status.HTTP_400_BAD_REQUEST,
            )

        # Filter active designations belonging to the selected departments
        designations = (
            Designation.objects
            .filter(
                department__id__in=department_ids,
                is_active=True,
            )
            .select_related("department")
            .order_by("department__dept_name", "designation_name")
        )

        serializer = DesignationSerializer(designations, many=True)

        return api_response(
            success=True,
            message=RETRIEVED_SUCCESSFULLY.format(DESIGNATION),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )