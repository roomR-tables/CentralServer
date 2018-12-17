from pyramid.view import (view_config)
from pyramid.httpexceptions import (HTTPMethodNotAllowed)


@view_config(route_name='cc_status', renderer='json')
def cc_status_view(request):
    if request.method == 'GET':
        cc_id = request.matchdict['id']

        return {
            'id': cc_id
        }

    raise HTTPMethodNotAllowed
