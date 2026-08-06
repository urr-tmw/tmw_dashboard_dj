from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from accounts.serializers.auth.refresh_token_serializer import (
    RefreshTokenSerializer,
)

from accounts.services.auth.refresh_token_service import (
    RefreshTokenService,
)

from utils.unified_response import api_response


class RefreshTokenAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RefreshTokenSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = RefreshTokenService.refresh(
            serializer.validated_data
        )

        return api_response(
            success=True,
            message="Token refreshed successfully.",
            data=data,
            http_status=status.HTTP_200_OK,
        )