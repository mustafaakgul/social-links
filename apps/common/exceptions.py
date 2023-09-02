from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


class Custom404Exception(APIException):
    status_code = 404
    default_detail = 'An error occurred.'
    default_code = 'error'


class Custom400Exception(APIException):
    status_code = 400
    default_detail = 'An error occurred.'
    default_code = 'error'


class ProjectBaseException(Exception):
    message = "Project Base Exception"
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    def __str__(self) -> str:
        return self.message
class AddressMaxLimitExceeded(ProjectBaseException):
    message = "Max address limit exceeded. Try inactive your addresses or delete."

# Usage of custom exception handler
def custom_exception_handler(exc, context):
    if isinstance(exc, Custom404Exception):
        response_data = {
            'code': exc.default_code,
            'detail': exc.default_detail
        }
        return Response(response_data, status=exc.status_code)
    return exception_handler(exc, context)

# def custom_exception_handler(exc: Exception, ctx: dict[str, Any]) -> Response:
#     response = drf_exception_handler(exc=exc, context=ctx)
#     if response is not None:
#         response_payload = {
#             "error": response.data,
#             "status_code": response.status_code,
#             "reason": http.client.responses.get(response.status_code),
#             "view_name": ctx["view"].__class__.__name__,
#             "view_desc": ctx["view"].__class__.__doc__,
#         }
#         response.data = response_payload
#     else:
#         if isinstance(exc, ProjectBaseException):
#             response_payload = {
#                 "details": exc.message,
#                 "status_code": exc.status_code,
#                 "reason": http.client.responses.get(exc.status_code),
#                 "view_name" : ctx["view"].__class__.__name__,
#                 "view_desc" : ctx["view"].__class__.__doc__,
#             }
#         return Response(data=response_payload, status=exc.status_code)
#     return response

# Solution 1 -> raise CustomException
# Solution 2 -> def my_view(request): raise APIException("There was a problem!")