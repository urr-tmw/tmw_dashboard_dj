
from rest_framework import status
from rest_framework.response import Response as DjangoRestResponse

def api_response(success: bool, message: str, data=None, error_details=None, http_status=status.HTTP_200_OK,meta=None):
    """
    Generate a unified API response structure.
    
    :param success: Boolean indicating success or failure
    :param message: String message to provide more context
    :param data: (Optional) Dictionary containing response data
    :param error_details: (Optional) Additional details about the error
    :param http_status: HTTP status code (default: 200 OK)
    :return: Django REST framework Response object
    
    """
    response_structure = {
        "success": success,
        "message": message,
        "data": data if data else {},
        "error_details": error_details if error_details else None,
        "meta": meta if meta else {}
    }

    return DjangoRestResponse(response_structure, status=http_status, content_type="application/json")
