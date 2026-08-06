from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """
    Login using Username or Email + Password
    """

    login = serializers.CharField(
        max_length=255,
        trim_whitespace=True,
    )

    password = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs):

        login = attrs.get("login")
        password = attrs.get("password")

        if not login:
            raise serializers.ValidationError(
                {
                    "login": "Username or Email is required."
                }
            )

        if not password:
            raise serializers.ValidationError(
                {
                    "password": "Password is required."
                }
            )

        attrs["login"] = login.strip()

        return attrs