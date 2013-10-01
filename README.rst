Flask-Sockets
=============

Elegant WebSockets for your Flask apps.


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

Serving WebSockets in Python were really difficult. Now they're not.


Deployment
----------

A custom Gunicorn worker is included to make deployment as friendly as possible::

    $ gunicorn -k flask_sockets.worker hello:app

Production services are provided by `gevent <http://www.gevent.org>`_
and `gevent-websocket <http://www.gelens.org/code/gevent-websocket/>`_.

Anything that inserts ``wsgi.websocket`` into the WSGI environ is
supported, but gevent-websocket is recommended.