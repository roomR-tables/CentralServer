from pyramid.view import (view_config)
from pyramid.httpexceptions import (HTTPBadRequest)


@view_config(route_name='cc_move', renderer='json')
def cc_move(request):
    if request.json_body.get('setup'):
        cc_id = request.matchdict['id']
        setup = request.json_body['setup']

        return {
            'id': cc_id,
            'setup': setup
        }
    else:
        raise HTTPBadRequest
