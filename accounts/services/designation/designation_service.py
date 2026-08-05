from django.db import transaction
from django.shortcuts import get_object_or_404

from accounts.models import Designation
from accounts.serializers.designation.designation_serializer import DesignationSerializer
from common.base_service import BaseMasterService




class DesignationService(BaseMasterService):

    model = Designation
    serializer_class = DesignationSerializer
    ordering_field = "designation_name"