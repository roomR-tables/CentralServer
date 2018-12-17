import os
import logging

from pyramid.config import Configurator
from central_server import views

logging.basicConfig()
log = logging.getLogger('waitress')

here = os.path.dirname(os.path.abspath(__file__))


def main(global_config, **settings):
    # configuration setup
    config = Configurator(settings=settings)

    # add mako templating
    config.include('pyramid_mako')

    # static files
    config.add_static_view(name='static', path='static')

    # Configure routes
    config.scan()
    config.add_route('home', '/')
    config.add_route('cc_home', '/cc/{id}')
    config.add_route('cc_status', '/cc/{id}/status')
    config.add_route('cc_move', '/cc/{id}/move')

    # serve central_server
    return config.make_wsgi_app()
