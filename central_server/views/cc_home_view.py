from pyramid.view import (view_config)
from pyramid.httpexceptions import (HTTPMethodNotAllowed)


@view_config(route_name='cc_home', renderer='cc_home.mako')
def cc_home_view(request):
    if request.method == 'GET':
        return {
            'id': request.matchdict['id']
        }

    raise HTTPMethodNotAllowed
