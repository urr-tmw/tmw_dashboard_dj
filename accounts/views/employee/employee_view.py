from rest_framework import status
from rest_framework.views import APIView

from accounts.permissions.dashboard_permission import DashboardPermission
from accounts.serializers.employee.employee_serializer import (
    EmployeeSerializer,
)
from accounts.services.employee.employee_service import EmployeeService

from common.constants import (
    CREATED_SUCCESSFULLY,
    UPDATED_SUCCESSFULLY,
    FETCHED_SUCCESSFULLY,
    LIST_FETCHED_SUCCESSFULLY,
    EMPLOYEE,
)
from accounts.serializers.employee.employee_create_serializer import (
    EmployeeCreateSerializer,
)

from accounts.services.employee.employee_create_service import (
    EmployeeCreateService,
)
from utils.unified_response import api_response


class EmployeeAPIView(APIView):
    """
    Employee CRUD APIs
    """

    permission_classes = [DashboardPermission]

    def get(self, request, employee_id=None):

        if employee_id:

            employee = EmployeeService.get_by_id(employee_id)

            serializer = EmployeeSerializer(employee)

            return api_response(
                success=True,
                message=FETCHED_SUCCESSFULLY.format(EMPLOYEE),
                data=serializer.data,
                http_status=status.HTTP_200_OK,
            )

        employees = EmployeeService.get_queryset()

        serializer = EmployeeSerializer(
            employees,
            many=True,
        )

        return api_response(
            success=True,
            message=LIST_FETCHED_SUCCESSFULLY.format(EMPLOYEE),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def post(self, request):
        """
        Create Employee (User + Employee + Roles)
        """

        serializer = EmployeeCreateSerializer(
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        employee = EmployeeCreateService.create_employee(
            serializer.validated_data,
        )

        response_serializer = EmployeeSerializer(employee)

        return api_response(
            success=True,
            message=CREATED_SUCCESSFULLY.format(EMPLOYEE),
            data=response_serializer.data,
            http_status=status.HTTP_201_CREATED,
        )

    def put(self, request, employee_id):

        employee = EmployeeService.update(
            employee_id,
            request.data,
        )

        serializer = EmployeeSerializer(employee)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(EMPLOYEE),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )

    def patch(self, request, employee_id):

        employee = EmployeeService.partial_update(
            employee_id,
            request.data,
        )

        serializer = EmployeeSerializer(employee)

        return api_response(
            success=True,
            message=UPDATED_SUCCESSFULLY.format(EMPLOYEE),
            data=serializer.data,
            http_status=status.HTTP_200_OK,
        )