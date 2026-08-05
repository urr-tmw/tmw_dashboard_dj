from django.db import transaction
from django.shortcuts import get_object_or_404
from common.base_service import BaseMasterService
from accounts.models import Department
from accounts.serializers.department.department_serializer import DepartmentSerializer



class DepartmentService(BaseMasterService):

    model = Department
    serializer_class = DepartmentSerializer
    ordering_field = "dept_name"