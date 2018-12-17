"""views"""

from pyramid.view import (view_config, exception_view_config)
from pyramid.httpexceptions import (HTTPBadRequest, HTTPMethodNotAllowed)


def includeme(config):
    """Add routes"""
    config.scan(__name__)
    config.add_route('home', '/')
    config.add_route('cc_home', '/cc/{id}')
    config.add_route('cc_status', '/cc/{id}/status')
    config.add_route('cc_move', '/cc/{id}/move')


@view_config(route_name='home', renderer='home.mako')
def home_view(request):
    if request.method == 'GET':
        return {}

    raise HTTPMethodNotAllowed


@view_config(route_name='cc_home', renderer='cc_home.mako')
def cc_home_view(request):
    if request.method == 'GET':
        return {
            'id': request.matchdict['id']
        }

    raise HTTPMethodNotAllowed


@view_config(route_name='cc_status', renderer='json')
def cc_status_view(request):
    if request.method == 'GET':
        cc_id = request.matchdict['id']

        return {
            'id': cc_id
        }

    raise HTTPMethodNotAllowed


@view_config(route_name='cc_move', renderer='json')
def cc_move(request):
    if request.method == 'POST':
        if request.json_body.get('setup'):
            cc_id = request.matchdict['id']
            setup = request.json_body['setup']

            return {
                'id': cc_id,
                'setup': setup
            }
        else:
            raise HTTPBadRequest

    raise HTTPMethodNotAllowed


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
