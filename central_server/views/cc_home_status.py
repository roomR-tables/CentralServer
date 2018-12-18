import time
import logging
from pyramid.httpexceptions import (HTTPGatewayTimeout, HTTPInternalServerError)
from pyramid.view import (view_config)
import paho.mqtt.client as mqtt

log = logging.getLogger("view.cc_home_status")


@view_config(route_name='cc_status', renderer='json')
def cc_status_view(request):
    global loop
    global status

    loop = True
    status = None

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        client.subscribe(topic='cc/' + request.matchdict['id'] + '/status', qos=1)
        client.publish(topic='cc/' + request.matchdict['id'] + '/cmd', payload='{"cmd": "request_status", "payload": ""}', qos=1)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        global loop
        global status

        status = msg.payload.decode("utf-8")
        loop = False

    client = mqtt.Client("server")
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(request.registry.settings["mqtt.hostname"], int(request.registry.settings["mqtt.port"]), 60)
    except ConnectionError as e:
        log.error("Error when connecting to the MQTT broker: %s", e)
        raise HTTPInternalServerError

    start_time = time.time()

    # Wait 30 seconds for a response
    while loop:
        client.loop()
        elapsed_time = time.time() - start_time

        if elapsed_time > 30:
            client.disconnect()
            loop = False
            break

    if status is None:
        raise HTTPGatewayTimeout
    else:
        return {
            'status': status
        }
