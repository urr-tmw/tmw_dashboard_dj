from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from accounts.serializers.auth.logout_serializer import LogoutSerializer
from accounts.services.auth.logout_service import LogoutService

from common.constants import LOGOUT_SUCCESSFUL

from utils.unified_response import api_response


class LogoutAPIView(APIView):
    """
    Dashboard Logout API
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = LogoutSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        LogoutService.logout(
            serializer.validated_data,
        )

        return api_response(
            success=True,
            message=LOGOUT_SUCCESSFUL,
            http_status=status.HTTP_200_OK,
        )