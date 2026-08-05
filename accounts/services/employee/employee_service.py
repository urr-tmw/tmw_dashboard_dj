from accounts.models import Employee
from accounts.serializers.employee.employee_serializer import (
    EmployeeSerializer,
)

from common.base_service import BaseMasterService


class EmployeeService(BaseMasterService):

    model = Employee

    serializer_class = EmployeeSerializer

    lookup_field = "employee_id"

    ordering_field = "employee_code"