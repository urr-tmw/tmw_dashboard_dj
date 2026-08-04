from django.http import Http404
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, NotAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import PermissionDenied

from utils.unified_response import api_response


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    # Let DRF handle anything it doesn't know about
    if response is None:
        return api_response(
            success=False,
            message="Something went wrong.",
            data={},
            error_details=str(exc),
            http_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    # Validation Errors
    if isinstance(exc, ValidationError):
        return api_response(
            success=False,
            message="Validation failed.",
            data={},
            error_details=response.data,
            http_status=response.status_code,
        )

    # Authentication Failed
    if isinstance(exc, AuthenticationFailed):
        return api_response(
            success=False,
            message="Authentication failed.",
            data={},
            error_details=response.data,
            http_status=response.status_code,
        )

    # Login Required
    if isinstance(exc, NotAuthenticated):
        return api_response(
            success=False,
            message="Authentication credentials were not provided.",
            data={},
            error_details=response.data,
            http_status=response.status_code,
        )

    # Permission Denied
    if isinstance(exc, PermissionDenied):
        return api_response(
            success=False,
            message="Permission denied.",
            data={},
            error_details=response.data,
            http_status=response.status_code,
        )

    # Object Not Found
    if isinstance(exc, Http404):
        return api_response(
            success=False,
            message="Resource not found.",
            data={},
            error_details=response.data,
            http_status=response.status_code,
        )

    # Any remaining DRF exception
    return api_response(
        success=False,
        message="Request failed.",
        data={},
        error_details=response.data,
        http_status=response.status_code,
    )