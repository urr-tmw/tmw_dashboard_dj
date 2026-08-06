from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


class RefreshTokenService:

    @staticmethod
    def refresh(validated_data):

        try:

            refresh = RefreshToken(
                validated_data["refresh"]
            )

            return {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }

        except TokenError:
            raise AuthenticationFailed(
                "Invalid or expired refresh token."
            )