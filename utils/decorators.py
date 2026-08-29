from functools import wraps

from rest_framework import status

from utils.unified_response import api_response


def validate_required_keys(
    required_keys,
    source="data",
    validate_values=None,
):
    """
    Validate required request keys and allowed values.

    Example:

        @validate_required_keys(
            required_keys=["phone", "message"],
            source="data",
        )

    Allowed values:

        @validate_required_keys(
            required_keys=["phone", "type"],
            source="data",
            validate_values={
                "type": ["sms", "whatsapp"]
            },
        )
    """

    def decorator(view_func):

        @wraps(view_func)
        def _wrapped_view(*args, **kwargs):

            # Support CBV and FBV
            if hasattr(args[0], "request"):
                # Class Based View
                request = args[0].request
            else:
                # Function Based View
                request = args[0]

            # Select request source
            if source == "data":
                incoming_data = request.data
            elif source == "query":
                incoming_data = request.GET
            else:
                return api_response(
                    success=False,
                    message="Invalid validation source.",
                    error_details={
                        "source": "Source must be either 'data' or 'query'."
                    },
                    http_status=status.HTTP_400_BAD_REQUEST,
                )

            # Required keys validation
            missing_keys = [
                key
                for key in required_keys
                if not incoming_data.get(key)
            ]

            if missing_keys:
                return api_response(
                    success=False,
                    message="Missing required keys",
                    error_details={
                        "missing_keys": missing_keys
                    },
                    http_status=status.HTTP_400_BAD_REQUEST,
                )

            # Allowed values validation
            if validate_values:

                for key, allowed_values in validate_values.items():

                    if (
                        key in incoming_data
                        and incoming_data[key] not in allowed_values
                    ):
                        return api_response(
                            success=False,
                            message=f"Invalid value for '{key}'",
                            error_details={
                                key: (
                                    f"Must be one of "
                                    f"{allowed_values}"
                                )
                            },
                            http_status=status.HTTP_400_BAD_REQUEST,
                        )

            return view_func(*args, **kwargs)

        return _wrapped_view

    return decorator