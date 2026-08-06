from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from accounts.services.auth.me_service import MeService

from common.constants import FETCHED_SUCCESSFULLY

from utils.unified_response import api_response


class MeAPIView(APIView):
    """
    Returns current authenticated user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

        data = MeService.get_profile(
            request.user,
        )

        return api_response(
            success=True,
            message=FETCHED_SUCCESSFULLY.format("Profile"),
            data=data,
            http_status=status.HTTP_200_OK,
        )