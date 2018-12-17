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
    config.include(views)

    # serve central_server
    return config.make_wsgi_app()
