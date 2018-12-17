from pyramid.view import (exception_view_config)
from pyramid.httpexceptions import (HTTPBadRequest, HTTPMethodNotAllowed)


@exception_view_config(HTTPBadRequest, renderer='json')
def exc_view_bad_request(message, request):
    body = {
        "message": str(message),
        "status": 400
    }
    request.response.status = 400
    return body


@exception_view_config(HTTPMethodNotAllowed, renderer='json')
def exc_view_method_now_allowed(message, request):
    body = {
        "message": "Method Not Allowed" if not str(message) else str(message),
        "status": 405
    }
    request.response.status = 405
    return body
