from pyramid.view import (view_config)
from paho.mqtt.subscribe import (simple)
from paho.mqtt.publish import (single)


@view_config(route_name='cc_status', renderer='json')
def cc_status_view(request):
    cc_id = request.matchdict['id']

    return {
        'id': cc_id
    }
