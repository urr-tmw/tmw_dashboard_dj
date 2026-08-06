from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutService:
    """
    Handles user logout by blacklisting the refresh token.
    """

    @staticmethod
    def logout(validated_data):

        refresh_token = validated_data.get("refresh")

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

        except TokenError:
            raise AuthenticationFailed(
                "Invalid or expired refresh token."
            )