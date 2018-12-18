from pyramid.view import (view_config)


@view_config(route_name='cc_home', renderer='cc_home.mako')
def cc_home_view(request):
    return {
        'id': request.matchdict['id']
    }
