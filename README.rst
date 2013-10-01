Flask-Sockets
=============

Elegant WebSockets for your Flask apps.


Serving WebSockets in Python were really difficult.

.. code-block:: python

    from flask import Flask
    from flask_sockets import Sockets

    app = Flask(__name__)
    sockets = Sockets(app)

    @sockets.route('/echo')
    def echo_socket(ws):
        while True:
            message = ws.receive()
            ws.send(message)

    @app.route('/')
    def hello():
        return 'Hello World!'

Now they're not.