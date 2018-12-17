import logging

from pyramid.config import Configurator
from central_server import views

logging.basicConfig()
log = logging.getLogger('central_server')


def main(global_config, **settings):
    # configuration setup
    config = Configurator(settings=settings)

    # add mako templating
    config.include('pyramid_mako')

    # static files
    config.add_static_view(name='static', path='static')

    # Configure routes
    config.scan()
    config.add_route('home', '/', request_method='GET')
    config.add_route('cc_home', '/cc/{id}', request_method='GET')
    config.add_route('cc_status', '/cc/{id}/status', request_method='GET')
    config.add_route('cc_move', '/cc/{id}/move', request_method='POST')

    # serve central_server
    return config.make_wsgi_app()
