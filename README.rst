Flask-WebSocket
===============

WebSockets in Python are really hard.

.. code-block:: python

    from flask import Flask
    from flask_websockets import WebSocket

    app = Flask(__name__)

    @websocket.route('/echo')
    def echo_socket(ws):
        while True:
            message = ws.receive()
            ws.send(message)

    @app.route('/')
    def hello():
        return 'Hello World!'

Now they're not.