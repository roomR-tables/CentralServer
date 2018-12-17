from pyramid.view import (view_config)
from pyramid.httpexceptions import (HTTPMethodNotAllowed)


@view_config(route_name='home', renderer='home.mako')
def home_view(request):
    if request.method == 'GET':
        return {}

    raise HTTPMethodNotAllowed
